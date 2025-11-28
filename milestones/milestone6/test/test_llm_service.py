"""Test for LLMModel."""

import os
import sys

# Add parent directory to path to allow importing modules
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from services.llm_service import LLMModel

def test_llm_service():
    print("Initializing LLM Model...")
    try:
        # Initialize LLM
        llm = LLMModel()
        
        # Test generation
        prompt = "Hello, who are you?"
        print(f"Sending prompt: '{prompt}'")
        
        response = llm.generate(prompt)
        print(f"Response:\n{response}")
        
    except Exception as e:
        print(f"Error testing LLM service: {e}")
        print("Make sure Ollama is running and the model is pulled.")

if __name__ == "__main__":
    test_llm_service()
