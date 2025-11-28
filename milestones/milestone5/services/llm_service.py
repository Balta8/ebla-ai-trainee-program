"""LLM integration using Ollama."""

from langchain_community.llms import Ollama
from config import settings
import logging

logger = logging.getLogger(__name__)


class LLMModel:
    """Wrapper for Ollama LLM."""
    
    def __init__(self):
        """
        Initialize the LLM model.
        """
        self.model_name = settings.llm_model_name
        self.base_url = settings.llm_base_url
        self.temperature = settings.llm_temperature

        try:
            self.llm = Ollama(
                model=self.model_name,
                base_url=self.base_url,
                temperature=self.temperature
            )
            logger.info(f"LLM initialized: {self.model_name} at {self.base_url}")
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


