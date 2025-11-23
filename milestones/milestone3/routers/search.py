"""Router for document search operations."""

from fastapi import APIRouter, HTTPException
from models.api_schemas import SearchRequest, SearchResponse
from controllers.document_controller import DocumentController
import logging

# Setup logger
logger = logging.getLogger(__name__)

# Create router
router = APIRouter()

# Initialize controller
controller = DocumentController()


@router.post("/search", response_model=SearchResponse, tags=["Search"])
async def search_documents(request: SearchRequest):
    """
    Search for relevant documents.
    
    Args:
        request: SearchRequest containing query and parameters
        
    Returns:
        SearchResponse with matching documents
        
    Raises:
        HTTPException: If search fails
    """
    try:
        logger.info(f"Search request: '{request.query}'")
        return controller.search_documents(request)
        
    except Exception as e:
        logger.error(f"Search failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")
