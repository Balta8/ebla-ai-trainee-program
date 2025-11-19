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

# Quick test
if __name__ == "__main__":
    docs = [
        "Python is a high-level programming language known for its simplicity and readability. It is widely used in web development, data science, artificial intelligence, and automation.",
        "Ebla Computer Consultancy provides innovative IT solutions including cloud computing and software development.",
        "Machine learning algorithms enable computers to learn from data without being explicitly programmed."
    ]
    View.show_documents(docs)
    
