"""Module for presenting results."""

from typing import List

class View:
    """Handles display of retrieved documents and model responses."""

    @staticmethod
    def show_documents(docs: List[str]) -> None:
        """Display retrieved document chunks."""
        print("🔍 Retrieved Documents:")
        for idx, doc in enumerate(docs, start=1):
            print(f"{idx}. {doc[:200]}…")

    @staticmethod
    def show_response(response: str) -> None:
        """Display the model's generated response."""
        print("💡 Model Response:")
        print(response)
