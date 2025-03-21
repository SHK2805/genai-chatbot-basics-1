from config.set_config import Config
from src.constants import gorq_model_name
from src.manager.chat_manager import ChatManager
from src.manager.chat_history_manager import ChatHistoryManager
from src.platforms.manager import PlatformManager
from src.platforms.types import PlatformTypes
from src.types.message_type import MessageType
from src.manager.dynamic_chat_session_manager import DynamicChatSessionManager

def initialize():
    """
    Initialize platform, history manager, chat manager, and dynamic session manager.
    """
    # Initialize Config
    config = Config()
    if config.set():
        print("Environment variables set")
    else:
        print("Environment variables NOT set")

    # Initialize Platform and Managers
    platform_manager = PlatformManager(PlatformTypes.GROQ)
    history_manager = ChatHistoryManager(platform_manager.get_llm(gorq_model_name))
    chat_manager = ChatManager(platform_manager, history_manager, gorq_model_name)
    dynamic_session_manager = DynamicChatSessionManager()

    return dynamic_session_manager, chat_manager


def main():
    """
    The main logic of the application for managing chat sessions dynamically.
    """
    # Initialize Managers
    dynamic_session_manager, chat_manager = initialize()

    # Create a new chat session
    session_id = "1234"
    dynamic_session_manager.add_session(session_id, chat_manager)

    # Add Messages to the session
    messages = [
        (MessageType.HUMAN, "Hello, this is Test User. I am a Data Scientist."),
        (MessageType.AI, "Hello Test User, how can I assist you today?"),
        (MessageType.HUMAN, "What is my name?"),
        (MessageType.AI, "You stated your name is Test User."),
        (MessageType.HUMAN, "What is my profession?"),
        (MessageType.AI, "You said you are a Data Scientist."),
        (MessageType.HUMAN, "Can you summarize our chat?")
    ]

    for message_type, content in messages:
        dynamic_session_manager.add_message(session_id, message_type, content)

    # Get a response for the session
    response = dynamic_session_manager.get_response(session_id, "English")
    print("Chat Response:", response)

    # Clear all sessions after chat
    dynamic_session_manager.clear_all_sessions()


if __name__ == "__main__":
    main()
