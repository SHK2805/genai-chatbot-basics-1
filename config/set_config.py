import os
from config.env_manager import groq_api_key

# this gets the key-values from the .env file and sets the environment
class Config:
    def __init__(self):
        self.groq_api_key = groq_api_key()

    def set(self):
        try:
            os.environ['GROQ_API_KEY'] = self.groq_api_key
        except Exception as e:
            print(f'Error setting environment variables: {e}')
            return False
        return True