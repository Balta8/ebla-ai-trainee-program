"""Main CLI application for document indexing and search."""

from controllers.document_controller import DocumentController
from views.cli_view import CLIView
from utils.logging_config import setup_logging
import sys
import os
import logging


def main():
    """Main entry point for CLI application."""
    # Setup logging (logs will be saved to logs/ directory)
    setup_logging(log_level=logging.INFO, log_to_file=True)
    logger = logging.getLogger(__name__)
    logger.info("Application started")
    
    view = CLIView()
    # Inject the view into the controller so it can display messages
    controller = DocumentController(view=view)
    
    print("\n" + "="*80)
    print("Document Indexing & Search System - CLI")
    print("="*80)
    
    while True:
        print("\n--- Menu ---")
        print("1. Index documents")
        print("2. Search documents")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            # Index documents
            documents_path = input("Enter documents directory path (default: data): ").strip()
            
            # Get script directory for relative path resolution
            script_dir = os.path.dirname(os.path.abspath(__file__))
            
            if not documents_path:
                # Use default
                documents_path = os.path.join(script_dir, "data")
            elif not os.path.isabs(documents_path):
                # Convert relative path to absolute based on script location
                documents_path = os.path.join(script_dir, documents_path)
            
            collection_name = input("Enter collection name (default: documents): ").strip()
            if not collection_name:
                collection_name = "documents"
            
            try:
                controller.index_documents(
                    documents_path=documents_path,
                    collection_name=collection_name
                )
            except Exception as e:
                view.show_error(f"Failed to index documents: {str(e)}")
        
        elif choice == "2":
            # Search documents
            query = input("Enter your search query: ").strip()
            if not query:
                view.show_error("Query cannot be empty")
                continue
            
            collection_name = input("Enter collection name (default: documents): ").strip()
            if not collection_name:
                collection_name = "documents"
            
            top_k_input = input("Number of results (default: 3): ").strip()
            try:
                top_k = int(top_k_input) if top_k_input else 3
                if top_k <= 0:
                    view.show_error("Number of results must be positive. Using default: 3")
                    top_k = 3
            except ValueError:
                view.show_error("Invalid number. Using default: 3")
                top_k = 3
            
            try:
                controller.search_documents(
                    query=query,
                    collection_name=collection_name,
                    top_k=top_k
                )
            except Exception as e:
                view.show_error(f"Failed to search documents: {str(e)}")
        
        elif choice == "3":
            view.show_success("Goodbye!")
            sys.exit(0)
        
        else:
            view.show_error("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()

