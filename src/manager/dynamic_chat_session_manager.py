from src.types.message_type import MessageType
from src.manager.chat_manager import ChatManager


class DynamicChatSessionManager:
    def __init__(self):
        self.sessions = {}  # A dictionary to track session-specific chat managers

    def add_session(self, session_id: str, chat_manager: ChatManager):
        """
        Adds a new session and associates it with a chat manager.
        """
        if session_id in self.sessions:
            raise ValueError(f"Session {session_id} already exists.")
        self.sessions[session_id] = chat_manager

    def add_message_to_session(self, session_id: str, message_type: MessageType, content: str):
        """
        Adds a message (Human or AI) to the specified session's chat manager.
        """
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} does not exist. Please add the session first.")

        chat_manager = self.sessions[session_id]
        chat_manager.add_message_to_session(session_id, message_type, content)

    def get_session_response(self, session_id: str) -> str:
        """
        Retrieves the chat response for the specified session.
        """
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} does not exist. Please add the session first.")

        chat_manager = self.sessions[session_id]
        return chat_manager.manage_chat(session_id)

    def clear_session(self, session_id: str):
        """
        Clears the specific session and removes its associated chat manager.
        """
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} does not exist.")

        # Clear session in the associated chat manager
        chat_manager = self.sessions[session_id]
        chat_manager.chat_service.clear_session(session_id)

        # Remove session from the manager
        del self.sessions[session_id]
        print(f"Session {session_id} cleared.")

    def clear_all_sessions(self):
        """
        Clears all sessions and their associated chat managers.
        """
        for session_id in list(self.sessions.keys()):
            chat_manager = self.sessions[session_id]
            chat_manager.chat_service.clear_session(session_id)

        self.sessions.clear()
        print("All sessions cleared.")
