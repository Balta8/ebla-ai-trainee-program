"""Module interacting with a local LLM via Ollama."""

from typing import Any
import ollama


class LocalLLM:
    """Interface for a locally running LLM."""

    def __init__(self, model_name: str = "qwen2.5:7b") -> None:
        """
        Initialize the LLM client.

        Args:
            model_name: Name of the model to run via Ollama.
        """
        self.model_name = model_name
        self._check_connection()

    def _check_connection(self) -> None:
        """Check if we can connect to Ollama."""
        try:
            # Simple connection test
            response = ollama.generate(model=self.model_name, prompt="test")
            print(f"Connected to Ollama with model: {self.model_name}")
        except Exception as e:
            print(f"Connection issue: {e}")
            print("Make sure Ollama is running: 'ollama serve'")

    def generate(self, prompt: str) -> str:
        """
        Generate a response from the local LLM.

        Args:
            prompt: The input prompt to the model.

        Returns:
            The generated text from the model.
        """
        try:
            response: Any = ollama.chat(
                model=self.model_name, 
                messages=[{"role": "user", "content": prompt}]
            )
            return response['message']['content']
        except Exception as e:
            return f"Error: {e}"


# Quick test
if __name__ == "__main__":
    llm = LocalLLM()
    response = llm.generate("Hello! Say something short.")
    print(f"Response: {response}")