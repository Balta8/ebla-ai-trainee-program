"""Document controller for orchestrating document operations."""

from models.document_loader import DocumentLoader
from models.text_processor import TextProcessor
from models.vector_store import VectorStoreManager
from views.base_view import BaseView, SilentView
from typing import List, Tuple, Dict, Any, Optional
from langchain_core.documents import Document


class DocumentController:
    """Controller for managing document indexing and search operations."""
    
    def __init__(self, persist_directory: str = "./chroma_db", view: Optional[BaseView] = None):
        """
        Initialize the document controller.
        
        Args:
            persist_directory: Directory for ChromaDB persistence
            view: Optional view instance for displaying output. 
                  If None, a SilentView is used (for API context).
        """
        self.vector_store_manager = VectorStoreManager(persist_directory)
        # Use the provided view, or fall back to SilentView
        self.view = view if view else SilentView()
    
    def index_documents(
        self,
        documents_path: str,
        collection_name: str = "documents",
        chunk_size: int = 500,
        chunk_overlap: int = 50
    ) -> Dict[str, Any]:
        """
        Index documents from a directory.
        
        Args:
            documents_path: Path to documents directory
            collection_name: Name for the ChromaDB collection
            chunk_size: Size of text chunks
            chunk_overlap: Overlap between chunks
            
        Returns:
            Dictionary with indexing statistics
        """
        try:
            self.view.show_info("Starting document indexing...")
            
            # Load documents
            self.view.show_message("Loading documents...")
            loader = DocumentLoader(documents_path)
            documents = loader.load_documents()
            self.view.show_success(f"Loaded {len(documents)} documents")
            
            # Process documents
            self.view.show_message("Splitting documents into chunks...")
            processor = TextProcessor(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
            chunks = processor.process_documents(documents)
            self.view.show_success(f"Created {len(chunks)} chunks")
            
            # Create vector store
            self.view.show_message("Generating embeddings and creating vector store...")
            vector_store = self.vector_store_manager.create(chunks, collection_name)
            self.view.show_success(f"Vector store created with collection '{collection_name}'")
            
            # Display statistics
            self.view.display_indexing_stats(len(documents), len(chunks), collection_name)
            
            return {
                "status": "success",
                "documents_indexed": len(documents),
                "chunks_created": len(chunks),
                "collection_name": collection_name
            }
            
        except Exception as e:
            self.view.show_error(f"Indexing failed: {str(e)}")
            raise
    
    def search_documents(
        self,
        query: str,
        collection_name: str = "documents",
        top_k: int = 3
    ) -> List[Tuple[Document, float]]:
        """
        Search for documents similar to the query.
        
        Args:
            query: Search query text
            collection_name: Name of the ChromaDB collection
            top_k: Number of results to return
            
        Returns:
            List of tuples (Document, similarity_score)
        """
        try:
            self.view.show_info(f"Searching for: '{query}'")
            
            # Load vector store
            vector_store = self.vector_store_manager.load(collection_name)
            
            # Perform search
            results = self.vector_store_manager.search(vector_store, query, k=top_k)
            
            # Display results
            self.view.display_search_results(results, query)
            
            return results
            
        except Exception as e:
            self.view.show_error(f"Search failed: {str(e)}")
            raise
