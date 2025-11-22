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
    def display_search_results(results: List[Tuple[Document, float]], query: str):
        """
        Display search results in a formatted way.
        
        Args:
            results: List of tuples (Document, similarity_score)
            query: The original search query
        """
        print(f"\n{'='*80}")
        print(f"🔍 Search Results for: '{query}'")
        print(f"{'='*80}\n")
        
        if not results:
            print("No results found.")
            return
        
        for i, (doc, score) in enumerate(results, 1):
            print(f"\nResult {i} (Score: {score:.4f})")
            print(f"{'-'*80}")
            print(f"Content:\n{doc.page_content[:300]}...")
            
            if doc.metadata:
                print(f"\nMetadata:")
                for key, value in doc.metadata.items():
                    print(f"  • {key}: {value}")
            
            print(f"{'-'*80}")
        
        print(f"\nFound {len(results)} relevant documents\n")
    
    @staticmethod
    def display_indexing_stats(num_docs: int, num_chunks: int, collection_name: str):
        """
        Display statistics after indexing.
        
        Args:
            num_docs: Number of documents processed
            num_chunks: Number of chunks created
            collection_name: Name of the collection
        """
        print(f"\n{'='*80}")
        print("Indexing Statistics")
        print(f"{'='*80}")
        print(f"  • Documents Loaded: {num_docs}")
        print(f"  • Chunks Created: {num_chunks}")
        print(f"  • Collection Name: {collection_name}")
        print(f"  • Status: Successfully indexed")
        print(f"{'='*80}\n")
