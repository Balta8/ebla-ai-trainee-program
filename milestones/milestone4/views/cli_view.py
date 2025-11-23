"""CLI view for displaying messages and results."""

from typing import List, Tuple, Any
from langchain_core.documents import Document
from .base_view import BaseView


class CLIView(BaseView):
    """CLI View for displaying messages and results."""
    
    @staticmethod
    def show_message(message: str):
        """Display a general message."""
        print(f"\n{message}")
    
    @staticmethod
    def show_success(message: str):
        """Display a success message."""
        print(f"{message}")
    
    @staticmethod
    def show_error(message: str):
        """Display an error message."""
        print(f"\n Error: {message}")
    
    @staticmethod
    def show_info(message: str):
        """Display an info message."""
        print(f"\n info:{message}")
    
    @staticmethod
    def display_rag_response(query: str, answer: str, sources: List[Tuple[Any, float]]):
        """
        Display RAG response with answer and sources.
        
        Args:
            query: User's question
            answer: Generated answer
            sources: List of source documents
        """
        print(f"\n{'='*80}")
        print(f"🤖 Question: {query}")
        print(f"{'='*80}")
        print(f"\nAnswer:\n{answer}\n")
        print(f"{'='*80}")
        print("📚 Sources Used:")
        
        for i, (doc, score) in enumerate(sources, 1):
            source_name = doc.metadata.get('source', 'Unknown') if doc.metadata else 'Unknown'
            print(f"\n{i}. {source_name} (Score: {score:.4f})")
            print(f"   Preview: {doc.page_content[:150]}...")
        print(f"\n{'='*80}\n")

