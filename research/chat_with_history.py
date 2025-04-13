from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_groq import ChatGroq

from config.set_config import Config
from research.constants import chat_messages1, config1
from src.constants import gorq_model_name

"""
ChatWithGroq2 is a class that provides a wrapper around the ChatGroq model.
ChatMessageHistory: Maintains the history of chat messages.
RunnableWithMessageHistory: A runnable that maintains the history of messages.
BaseChatMessageHistory: An abstract class for chat message history. It is the collection of ChatMessageHistory.
"""

class ChatWithGroq2:
    def __init__(self, model_name: str = gorq_model_name):
        self.class_name: str = self.__class__.__name__
        self.model_name = model_name
        self.model = ChatGroq(model=model_name)
        self.initialize_environment()
        self.store = {}

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

    def get_model(self):
        """
        Get the model.
        """
        return self.model

    def get_model_name(self):
        """
        Get the model name.
        """
        return self.model_name

    def set_model(self, model_name: str = gorq_model_name):
        """
        Set the model.
        """
        self.model_name = model_name
        self.model = ChatGroq(model=model_name)

    def get_store(self):
        """
        Get the store.
        """
        return self.store

    def get_session_history(self, session_id: str = None) -> BaseChatMessageHistory:
        """
        Get the session history.
        """
        if  session_id is None:
            raise ValueError("Session ID is required")

        if session_id not in self.store:
            self.store[session_id] = ChatMessageHistory()

        return self.store[session_id]

    def runnable_with_history(self) -> RunnableWithMessageHistory:
        """
        Get the runnable with history.
        """
        return RunnableWithMessageHistory(self.model, self.get_session_history)


if __name__ == "__main__":
    chat = ChatWithGroq2()
    response1 = chat.runnable_with_history().invoke(
        chat_messages1,
        config=config1
    )
    # print(response1.content)
    ai_message1 = AIMessage(content=response1.content)
    human_message1 = HumanMessage(content="What am I asking you about?")
    message1 = [
        ai_message1,
        human_message1
    ]

    response2 = chat.runnable_with_history().invoke(
        message1,
        config=config1
    )
    print(response2.content)