"""Module for interacting with local LLM via Ollama."""

from llama_index.llms.ollama import Ollama
import sys

class LocalLLM:
    """Wrapper for Ollama LLM interaction."""
    
    def __init__(self, model_name: str = "qwen2.5:7b", timeout: float = 120.0) -> None:
        """
        Initialize the LocalLLM wrapper.
        
        Args:
            model_name: Name of the Ollama model to use.
            timeout: Request timeout in seconds.
        """
        self.model_name = model_name
        self.llm = Ollama(model=model_name, request_timeout=timeout)
        
    def check_connection(self) -> bool:
        """
        Check if connection to Ollama is working.
        
        Returns:
            bool: True if connected, False otherwise.
        """
        try:
            # Try a simple generation to test connection
            response = self.llm.complete("Hello")
            print(f"Connected to Ollama with model: {self.model_name}")
            return True
        except Exception as e:
            print(f"Failed to connect to Ollama: {str(e)}")
            return False
            
    def generate(self, prompt: str) -> str:
        """
        Generate text from a prompt.
        
        Args:
            prompt: Input prompt.
            
        Returns:
            Generated text response.
        """
        try:
            response = self.llm.complete(prompt)
            return str(response)
        except Exception as e:
            return f"Error generating response: {str(e)}"

# Standalone test execution
if __name__ == "__main__":
    llm = LocalLLM()
    if llm.check_connection():
        while True:
            prompt = input("\nEnter your prompt (or 'quit' to exit): ")
            if prompt.lower() in ['quit', 'exit', 'q']:
                break
            
            print("\nGenerating response...")
            response = llm.generate(prompt)
            print(f"\nResponse: {response}")
