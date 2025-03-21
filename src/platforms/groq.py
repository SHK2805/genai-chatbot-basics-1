from src.platforms.base import BaseLLM, BaseEmbedding
from langchain_groq import ChatGroq


class GROQModel(BaseLLM):
    def get_model(self, model_name):
        return ChatGroq(model=model_name)

class GROQEmbedding(BaseEmbedding):
    def get_embeddings(self, model_name):
        return None
