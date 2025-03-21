from src.types.message_type import MessageType
from langchain_core.messages import HumanMessage, AIMessage


class DynamicChatSessionManager:
    def __init__(self):
        self.sessions = {}

    def add_session(self, session_id: str, chat_manager):
        """
        Add a session with an associated ChatManager.
        """
        if session_id in self.sessions:
            raise ValueError(f"Session {session_id} already exists.")
        self.sessions[session_id] = chat_manager

    def add_message(self, session_id: str, message_type: MessageType, content: str):
        """
        Add a message to the session's ChatManager.
        """
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} does not exist.")

        if message_type == MessageType.HUMAN:
            message = HumanMessage(content=content)
        elif message_type == MessageType.AI:
            message = AIMessage(content=content)
        else:
            raise ValueError("Invalid message type.")

        self.sessions[session_id].add_message(session_id, message)

    def get_response(self, session_id: str, language: str) -> str:
        """
        Get a response for the given session ID.
        """
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} does not exist.")
        return self.sessions[session_id].get_response(session_id, language)

    def clear_session(self, session_id: str):
        """
        Clear the session's chat history and remove it.
        """
        if session_id not in self.sessions:
            raise ValueError(f"Session {session_id} does not exist.")
        del self.sessions[session_id]
        print(f"Session {session_id} cleared.")

    def clear_all_sessions(self):
        """
        Clear all sessions and their associated chat managers.
        """
        # Iterate over all sessions and remove them
        for session_id in list(self.sessions.keys()):
            del self.sessions[session_id]
        print("All sessions cleared.")
