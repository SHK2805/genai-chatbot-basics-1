from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables import RunnablePassthrough
from operator import itemgetter

class ChatManager:
    def __init__(self, platform_manager, history_manager, llm_name):
        self.history_manager = history_manager
        self.prompt = ChatPromptTemplate(
            [
                ("system", "You are a helpful assistant. Respond to my questions in the language {language}"),
                MessagesPlaceholder(variable_name="messages")
            ]
        )
        self.llm = platform_manager.get_llm(llm_name)

        # Define the chain
        self.chain = (
            RunnablePassthrough.assign(messages=itemgetter("messages"))
            | self.prompt
            | self.llm
        )

    def add_message(self, session_id: str, message: HumanMessage or AIMessage):
        """
        Add a message to the session history via ChatHistoryManager.
        """
        self.history_manager.add_message(session_id, message)

    def get_response(self, session_id: str, language: str) -> str:
        """
        Generate a response using the trimmed message history.
        """
        trimmed_history = self.history_manager.get_trimmed_history(session_id)
        response = self.chain.invoke({"messages": trimmed_history, "language": language})
        return response.content
