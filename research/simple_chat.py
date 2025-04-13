from langchain_groq import ChatGroq

from config.set_config import Config
from research.constants import user_message1, chat_messages1
from src.constants import gorq_model_name


class ChatWithGroq1:
    def __init__(self, model_name: str = gorq_model_name):
        self.class_name: str = self.__class__.__name__
        self.model_name = model_name
        self.model = ChatGroq(model=model_name)
        self.initialize_environment()

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

    def chat_with_groq(self, message):
        """
        Chat with the Groq model.
        """
        return self.model.invoke(message)
            

if __name__ == "__main__":
    chat = ChatWithGroq1()
    response = chat.chat_with_groq(user_message1)
    print(f"GORQ: {response.content}")

    response = chat.chat_with_groq(chat_messages1)
    print(f"GORQ: {response.content}")