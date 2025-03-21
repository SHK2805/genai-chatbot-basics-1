from abc import ABC, abstractmethod

# Abstract base class for LLMs
class BaseLLM(ABC):
    @abstractmethod
    def get_model(self, model_name):
        """Fetches the LLM model."""
        pass

# Abstract base class for Embeddings
class BaseEmbedding(ABC):
    @abstractmethod
    def get_embeddings(self, model_name):
        """Fetches the embedding model."""
        pass