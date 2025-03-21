from langchain_core.messages import HumanMessage, AIMessage

from src.types.message_type import MessageType


class ChatService:
    def __init__(self):
        self.sessions = {}  # Store messages for each session

    def add_message(self, session_id: str, message_type: MessageType, content: str) -> None:
        """
        Add a HumanMessage or AIMessage to the session's message list based on the MessageType enum.
        """
        if session_id not in self.sessions:
            self.sessions[session_id] = []  # Initialize session if not present

        if message_type == MessageType.HUMAN:
            self.sessions[session_id].append(HumanMessage(content=content))
        elif message_type == MessageType.AI:
            self.sessions[session_id].append(AIMessage(content=content))
        else:
            raise ValueError(f"Invalid message type: {message_type}. Use MessageType.HUMAN or MessageType.AI.")

    def get_session_messages(self, session_id: str) -> list:
        """
        Retrieve all messages for a specific session.
        """
        if session_id not in self.sessions:
            raise ValueError(f"No session found for session_id: {session_id}")
        return self.sessions[session_id]

    def clear_session(self, session_id: str) -> None:
        """
        Clear all messages for a specific session.
        """
        if session_id in self.sessions:
            del self.sessions[session_id]
