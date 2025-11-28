"""Index router for document indexing endpoint."""

from fastapi import APIRouter, HTTPException
from schemas.api_schemas import IndexRequest, IndexResponse
from controllers.document_controller import DocumentController
import os
import logging

logger = logging.getLogger(__name__)
router = APIRouter()
controller = DocumentController()


@router.post("/index", response_model=IndexResponse, tags=["Indexing"])
async def index_documents(request: IndexRequest):
    """
    Index documents from a directory.
    
    This endpoint:
    1. Loads all text and PDF files from the specified directory
    2. Splits them into manageable chunks
    3. Generates embeddings using HuggingFace model
    4. Stores them in ChromaDB vector store
    
    Args:
        request: IndexRequest containing documents_path, collection_name, chunk_size, and chunk_overlap
        
    Returns:
        IndexResponse with indexing statistics
        
    Raises:
        HTTPException: If indexing fails or path doesn't exist
    """
    try:
        logger.info(f"Indexing request received: path={request.documents_path}, collection={request.collection_name}")
        
        # Resolve path (convert relative to absolute based on app.py location)
        documents_path = request.documents_path
        if not os.path.isabs(documents_path):
            # Get the directory where app.py is located
            app_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            documents_path = os.path.join(app_dir, documents_path)
            logger.info(f"Resolved relative path to: {documents_path}")
        
        # Validate path exists
        if not os.path.exists(documents_path):
            logger.error(f"Path not found: {documents_path}")
            raise HTTPException(
                status_code=404,
                detail=f"Documents path not found: {documents_path}"
            )
        
        # Index documents
        result = controller.index_documents(
            documents_path=documents_path,  # Use resolved path
            collection_name=request.collection_name,
            chunk_size=request.chunk_size,
            chunk_overlap=request.chunk_overlap
        )
        
        logger.info(f"Indexing completed: {result['documents_indexed']} docs, {result['chunks_created']} chunks")
        
        return IndexResponse(
            status="success",
            message="Documents indexed successfully",
            documents_indexed=result["documents_indexed"],
            chunks_created=result["chunks_created"],
            collection_name=result["collection_name"]
        )
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Indexing failed: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Indexing failed: {str(e)}"
        )
