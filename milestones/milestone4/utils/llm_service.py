"""LLM integration using Ollama."""

from langchain_community.llms import Ollama
import logging

logger = logging.getLogger(__name__)


class LLMModel:
    """Wrapper for Ollama LLM."""
    
    def __init__(
        self,
        model_name: str = "qwen2.5:7b",
        base_url: str = "http://localhost:11434",
        temperature: float = 0.7
    ):
        """
        Initialize the LLM model.
        
        Args:
            model_name: Name of the Ollama model
            base_url: Ollama server URL
            temperature: Sampling temperature (0.0 to 1.0)
        """
        self.model_name = model_name
        self.base_url = base_url
        self.temperature = temperature
        
        try:
            self.llm = Ollama(
                model=model_name,
                base_url=base_url,
                temperature=temperature
            )
            logger.info(f"LLM initialized: {model_name} at {base_url}")
        except Exception as e:
            logger.error(f"Failed to initialize LLM: {str(e)}")
            raise
    
    def generate(self, prompt: str) -> str:
        """
        Generate text based on the prompt.
        
        Args:
            prompt: Input prompt for the LLM
            
        Returns:
            Generated text response
        """
        try:
            logger.info(f"Generating response for prompt (length: {len(prompt)} chars)")
            response = self.llm.invoke(prompt)
            logger.info(f"Response generated (length: {len(response)} chars)")
            return response
        except Exception as e:
            logger.error(f"Generation failed: {str(e)}")
            raise


# Example usage
if __name__ == "__main__":
    # Initialize LLM
    llm = LLMModel()
    
    # Test generation
    print(llm.generate("Hello, who are you?"))
