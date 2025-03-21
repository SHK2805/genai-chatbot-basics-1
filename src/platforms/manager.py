from src.platforms.groq import GROQModel, GROQEmbedding
from src.platforms.types import PlatformTypes


class PlatformManager:
    def __init__(self, platform_type: PlatformTypes):
        """Initialize PlatformManager with a specific platform type."""
        # Define the platform map for models and embeddings
        self.platform_map = {
            PlatformTypes.GROQ: (GROQModel, GROQEmbedding),
        }

        # Validate the platform type
        if platform_type not in self.platform_map:
            raise ValueError(f"Unsupported platform type: {platform_type}")

        # Dynamically set the platform classes based on the platform type
        self.platform_type = platform_type
        self.llm_class, self.embedding_class = self.platform_map[platform_type]

        # Initialize the LLM and embedding instances
        self.llm_instance = self.llm_class()
        self.embedding_instance = self.embedding_class()

    def get_llm(self, model_name=None):
        """Fetches the LLM model for the platform."""
        if not model_name:
            raise ValueError("Model name cannot be None")
        return self.llm_instance.get_model(model_name)

    def get_embedding(self, embedding_name=None):
        """Fetches the embedding model for the platform."""
        if not embedding_name:
            raise ValueError("Embedding name cannot be None")
        return self.embedding_instance.get_embeddings(embedding_name)


"""
# Usage
# Initialize PlatformManager for GROQ
platform_manager = PlatformManager(PlatformTypes.GROQ)
llm = platform_manager.get_llm("gpt-4")  # Fetch LLM
embedding = platform_manager.get_embedding("text-embedding-ada-002")  # Fetch embedding
"""
