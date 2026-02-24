
from langchain_community.chat_models import ChatOllama


def get_llm(
    temperature: float = 0,
    max_tokens: int = 256,
    model_name: str = "phi",  
):
    """
    Returns a configured Ollama LLM instance.
    
    Args:
        temperature: Controls randomness (0 = deterministic)
        max_tokens: Maximum tokens to generate
        model_name: Ollama model name (phi, gemma:2b, mistral, etc.)
    """
    return ChatOllama(
        model=model_name,
        temperature=temperature,
        num_predict=max_tokens,
    )