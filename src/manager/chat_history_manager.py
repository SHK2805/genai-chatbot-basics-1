from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.chat_message_histories import ChatMessageHistory
from src.manager.trimmer_manager import TrimmerManager


class ChatHistoryManager:
    def __init__(self, llm):
        self._store = {}
        self._trimmer_config = TrimmerManager(token_counter=llm)

    def get_chat_message_history(self, session_id: str) -> ChatMessageHistory:
        """
        Retrieve or create a chat message history for a given session ID.
        """
        if session_id not in self._store:
            self._store[session_id] = ChatMessageHistory()
        return self._store[session_id]

    def add_message(self, session_id: str, message: HumanMessage or AIMessage):
        """
        Add a message to the session's chat history.
        """
        if session_id not in self._store:
            self._store[session_id] = ChatMessageHistory()
        self._store[session_id].add_message(message)

    def get_trimmed_history(self, session_id: str) -> list:
        """
        Retrieve the trimmed message history for the given session ID.
        """
        if session_id not in self._store:
            raise ValueError(f"No chat history found for session ID: {session_id}")

        # Use the TrimmerConfig to trim messages
        messages = self._store[session_id].messages
        return self._trimmer_config.trim(messages)
