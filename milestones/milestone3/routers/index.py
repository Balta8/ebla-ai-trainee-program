"""Router for document indexing operations."""

from fastapi import APIRouter, HTTPException
from models.api_schemas import IndexRequest, IndexResponse
from controllers.document_controller import DocumentController
import logging

# Setup logger
logger = logging.getLogger(__name__)

# Create router
router = APIRouter()

# Initialize controller
controller = DocumentController()


@router.post("/index", response_model=IndexResponse, tags=["Indexing"])
async def index_documents(request: IndexRequest):
    """
    Index documents from a specified directory.
    
    Args:
        request: IndexRequest containing path and parameters
        
    Returns:
        IndexResponse with statistics
        
    Raises:
        HTTPException: If indexing fails
    """
    try:
        logger.info(f"Indexing request for path: {request.documents_path}")
        return controller.index_documents(request)
        
    except FileNotFoundError as e:
        logger.error(f"Path not found: {str(e)}")
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        logger.error(f"Indexing failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Indexing failed: {str(e)}")
