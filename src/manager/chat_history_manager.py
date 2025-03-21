from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory

# Global store for managing chat histories
CHAT_HISTORY_STORE = {}

class ChatHistoryManager:
    def get_chat_message_history(self, session_id: str) -> BaseChatMessageHistory:
        """
        Retrieve or create a chat message history for a given session ID.
        Uses a global variable to store session histories.
        """
        if session_id is None:
            raise ValueError("session_id is required")

        # Access the global store to retrieve or create chat history
        if session_id not in CHAT_HISTORY_STORE:
            CHAT_HISTORY_STORE[session_id] = ChatMessageHistory()
        return CHAT_HISTORY_STORE[session_id]

    def clear_chat_history(self, session_id: str) -> None:
        """
        Clear the chat history for a specific session ID.
        """
        if session_id in CHAT_HISTORY_STORE:
            del CHAT_HISTORY_STORE[session_id]

    def clear_all_histories(self) -> None:
        """
        Clear all stored chat histories.
        """
        CHAT_HISTORY_STORE.clear()
