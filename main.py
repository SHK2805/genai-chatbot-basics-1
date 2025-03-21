from config.set_config import Config
from src.manager.chat_manager import ChatManager
from src.manager.chat_history_manager import ChatHistoryManager
from src.platforms.manager import PlatformManager
from src.platforms.types import PlatformTypes
from src.types.message_type import MessageType
from src.manager.dynamic_chat_session_manager import DynamicChatSessionManager

# Initialize Config
config = Config()
if config.set():
    print("Environment variables set")
else:
    print("Environment variables NOT set")

# Initialize Platform and Managers
platform_manager = PlatformManager(PlatformTypes.GROQ)
chat_history_manager = ChatHistoryManager()
chat_manager_1 = ChatManager(platform_manager, chat_history_manager)
session1 = "[1]"

chat_history_manager_2 = ChatHistoryManager()
chat_manager_2 = ChatManager(platform_manager, chat_history_manager_2)
session2 = "[2]"

# Initialize Dynamic Chat Session Manager
dynamic_session_manager = DynamicChatSessionManager()

# Add Chat Sessions
dynamic_session_manager.add_session(session1, chat_manager_1)
dynamic_session_manager.add_session(session2, chat_manager_2)

# Add Messages to Session 1
dynamic_session_manager.add_message_to_session(session1, MessageType.HUMAN, "Hello, this is Test User. I am a Data Scientist.")
dynamic_session_manager.add_message_to_session(session1, MessageType.AI, "Hello Test User, how can I assist you today?")
dynamic_session_manager.add_message_to_session(session1, MessageType.HUMAN, "Can you tell me what my name is?")
dynamic_session_manager.add_message_to_session(session1, MessageType.AI, "According to your introduction, your name is Test User.")
dynamic_session_manager.add_message_to_session(session1, MessageType.AI, "Can you tell me what my profession is?")

# Add Messages to Session 2
dynamic_session_manager.add_message_to_session(session2, MessageType.HUMAN, "Can you tell me what my name is?")

# Get Responses for Each Session
response_1 = dynamic_session_manager.get_session_response(session1)
print(f"Response for Session {session1}:", response_1)

response_2 = dynamic_session_manager.get_session_response(session2)
print(f"Response for Session {session2}:", response_2)

# Clear a specific session
dynamic_session_manager.clear_session(session1)

# Clear all sessions
dynamic_session_manager.clear_all_sessions()
