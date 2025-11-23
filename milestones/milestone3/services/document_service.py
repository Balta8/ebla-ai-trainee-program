"""Document service for business logic."""

from utils.document_loader import DocumentLoader
from utils.text_processor import TextProcessor
from services.vector_store import VectorStoreManager
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)


class DocumentService:
    """Service layer for document operations."""
    
    def __init__(self, vector_store_manager: VectorStoreManager):
        """
        Initialize the service.
        
        Args:
            vector_store_manager: VectorStoreManager instance
        """
        self.vector_store_manager = vector_store_manager
    
    def index_documents(
        self,
        documents_path: str,
        collection_name: str,
        chunk_size: int,
        chunk_overlap: int
    ) -> Dict[str, Any]:
        """
        Index documents from a directory.
        
        Args:
            documents_path: Absolute path to documents
            collection_name: ChromaDB collection name
            chunk_size: Size of text chunks
            chunk_overlap: Overlap between chunks
            
        Returns:
            Dictionary with indexing statistics
        """
        # Load documents
        loader = DocumentLoader(documents_path)
        documents = loader.load_documents()
        
        # Process documents
        processor = TextProcessor(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        chunks = processor.process_documents(documents)
        
        # Create vector store
        self.vector_store_manager.create(chunks, collection_name)
        
        return {
            "documents_indexed": len(documents),
            "chunks_created": len(chunks),
            "collection_name": collection_name
        }
    
    def search_documents(
        self,
        query: str,
        collection_name: str,
        top_k: int
    ) -> List[Dict[str, Any]]:
        """
        Search documents and format results.
        
        Args:
            query: Search query
            collection_name: ChromaDB collection name
            top_k: Number of results
            
        Returns:
            List of formatted search results
        """
        # Load vector store and search
        vector_store = self.vector_store_manager.load(collection_name)
        results = self.vector_store_manager.search(vector_store, query, k=top_k)
        
        # Format results (business logic)
        formatted_results = [
            {
                "content": doc.page_content,
                "metadata": doc.metadata,
                "score": float(score)
            }
            for doc, score in results
        ]
        
        return formatted_results
