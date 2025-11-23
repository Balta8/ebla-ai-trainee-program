"""Document controller for orchestrating document operations."""

from services.document_service import DocumentService
from services.vector_store import VectorStoreManager
from views.base_view import BaseView, SilentView
from models.api_schemas import IndexRequest, IndexResponse, SearchRequest, SearchResponse, DocumentResult
from typing import Optional
import os
from utils.file_utils import resolve_path


class DocumentController:
    """Controller for managing document indexing and search operations."""
    
    def __init__(self, view: Optional[BaseView] = None):
        """
        Initialize the document controller.
        
        Args:
            view: Optional view instance. If None, SilentView is used (for API context).
        """
        self.vector_store_manager = VectorStoreManager()
        self.service = DocumentService(self.vector_store_manager)
        self.view = view if view else SilentView()
    
    def index_documents(self, request: IndexRequest) -> IndexResponse:
        """
        Index documents from a directory.
        
        Args:
            request: IndexRequest model
            
        Returns:
            IndexResponse model
        """
        try:
            self.view.show_info("Starting document indexing...")
            
            # Resolve and validate path
            resolved_path = resolve_path(request.documents_path)
            if not os.path.exists(resolved_path):
                error_msg = f"Documents path not found: {resolved_path}"
                self.view.show_error(error_msg)
                raise FileNotFoundError(error_msg)
            
            self.view.show_message("Loading documents...")
            
            # Call service
            result = self.service.index_documents(
                documents_path=resolved_path,
                collection_name=request.collection_name,
                chunk_size=request.chunk_size,
                chunk_overlap=request.chunk_overlap
            )
            
            self.view.show_success(f"Indexed {result['documents_indexed']} documents")
            self.view.display_indexing_stats(
                result["documents_indexed"],
                result["chunks_created"],
                result["collection_name"]
            )
            
            return IndexResponse(
                status="success",
                message="Documents indexed successfully",
                documents_indexed=result["documents_indexed"],
                chunks_created=result["chunks_created"],
                collection_name=result["collection_name"]
            )
            
        except Exception as e:
            self.view.show_error(f"Indexing failed: {str(e)}")
            raise
    
    def search_documents(self, request: SearchRequest) -> SearchResponse:
        """
        Search for documents similar to the query.
        
        Args:
            request: SearchRequest model
            
        Returns:
            SearchResponse model
        """
        try:
            self.view.show_info(f"Searching for: '{request.query}'")
            
            # Call service
            results = self.service.search_documents(
                query=request.query,
                collection_name=request.collection_name,
                top_k=request.top_k
            )
            
            self.view.show_success(f"Found {len(results)} results")
            
            # Convert to Pydantic models
            document_results = [
                DocumentResult(**doc_dict)
                for doc_dict in results
            ]
            
            return SearchResponse(
                status="success",
                query=request.query,
                results=document_results,
                total_results=len(document_results)
            )
            
        except Exception as e:
            self.view.show_error(f"Search failed: {str(e)}")
            raise
    

