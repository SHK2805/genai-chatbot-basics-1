from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, trim_messages
from config.set_config import Config
from research.constants import system_prompt, chat_messages2, config1
from src.constants import gorq_model_name

"""
ChatWithGroq2 is a class that provides a wrapper around the ChatGroq model.
ChatMessageHistory: Maintains the history of chat messages.
RunnableWithMessageHistory: A runnable that maintains the history of messages.
BaseChatMessageHistory: An abstract class for chat message history. It is the collection of ChatMessageHistory.
"""

class ChatWithGroq3:
    def __init__(self, model_name: str = gorq_model_name):
        self.class_name: str = self.__class__.__name__
        self.model_name = model_name
        self.model = ChatGroq(model=model_name)
        self.store = {}
        self.initialize_environment()

    def initialize_environment(self):
        """
        Initialize the environment.
        """
        # Initialize Config
        tag: str = f"[{self.class_name}]::initialize_environment"
        config = Config()
        if config.set():
            print(f"{tag}::Environment variables set")
        else:
            print(f"{tag}::Environment variables NOT set")

    def get_session_history(self, session_id: str = None) -> BaseChatMessageHistory:
        """
        Get the session history.
        """
        if  session_id is None:
            raise ValueError("Session ID is required")

        if session_id not in self.store:
            self.store[session_id] = ChatMessageHistory()

        return self.store[session_id]

    def runnable_with_chain(self, chat_chain: ChatPromptTemplate) -> RunnableWithMessageHistory:
        """
        Get the runnable with history.
        """
        if not chat_chain:
            raise ValueError("Chat chain is required")
        return RunnableWithMessageHistory(chat_chain, self.get_session_history)

    def get_chain(self, chat_history: list) -> ChatPromptTemplate:
        """
        Get the prompt.
        """
        if not chat_history or len(chat_history) == 0:
            raise ValueError("Chat history is required")
        prompt = ChatPromptTemplate.from_messages(chat_history)
        return prompt | self.model

class TrimmedChatMessageHistory(ChatMessageHistory):
    """
    A class that trims the chat message history.
    """
    def __init__(self):
        super().__init__()
        self.trimmer = trim_messages(max_tokens=1000,
                                     strategy="last",
                                     token_counter=self.model,
                                     include_system=True,
                                     allow_partial=False,
                                     start_on="human",)


if __name__ == "__main__":
    chat = ChatWithGroq3()
    chain = chat.get_chain(system_prompt)
    response = chain.invoke({"messages": chat_messages2}, config=config1)
    # print(f"Response: {response.content}")
    new_message = chat_messages2
    new_message.append(AIMessage(content=response.content))
    new_message.append(HumanMessage(content="Can you suggest a name to my restaurant."))
    response_with_history = chat.runnable_with_chain(chain).invoke(new_message, config=config1)
    # print(f"Response with history: {response_with_history.content}")
    new_message.append(AIMessage(content=response_with_history.content))
