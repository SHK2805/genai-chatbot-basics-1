from langchain_core.runnables import RunnableWithMessageHistory

from src.manager.chat_history_manager import ChatHistoryManager
from src.platforms.manager import PlatformManager
from src.constants import gorq_model_name
from src.services.chat_service import ChatService
from src.types.message_type import MessageType


class ChatManager:
    def __init__(self, platform_manager: PlatformManager, chat_history_manager: ChatHistoryManager):
        self.llm = platform_manager.get_llm(gorq_model_name)
        self.chat_service = ChatService()  # Use the updated ChatService
        self.chat_history_manager = chat_history_manager

    def add_message_to_session(self, session_id: str, message_type: MessageType, content: str) -> None:
        """
        Add a message to a session through the chat service.
        """
        self.chat_service.add_message(session_id=session_id, message_type=message_type, content=content)

    def manage_chat(self, session_id: str) -> str:
        """
        Manage chat flow dynamically using the session's stored messages.
        """
        messages = self.chat_service.get_session_messages(session_id)
        chat_history = self.chat_history_manager.get_chat_message_history(session_id)

        with_message_history = RunnableWithMessageHistory(self.llm, lambda x: chat_history)
        config = {'configurable': {'session_id': session_id}}
        response = with_message_history.invoke(input=messages, config=config)
        return response.content
