"""Search router for document search endpoint."""

from fastapi import APIRouter, HTTPException
from schemas.api_schemas import SearchRequest, SearchResponse, DocumentResult
from controllers.document_controller import DocumentController
import logging

logger = logging.getLogger(__name__)
router = APIRouter()
controller = DocumentController()


@router.post("/search", response_model=SearchResponse, tags=["Search"])
async def search_documents(request: SearchRequest):
    """
    Search for documents similar to the query.
    
    This endpoint:
    1. Loads the specified ChromaDB collection
    2. Generates embedding for the query
    3. Finds top-k most similar documents
    4. Returns results with similarity scores
    
    Args:
        request: SearchRequest containing query, collection_name, and top_k
        
    Returns:
        SearchResponse with matching documents and scores
        
    Raises:
        HTTPException: If search fails or collection doesn't exist
    """
    try:
        logger.info(f"Search request received: query='{request.query}', collection={request.collection_name}, top_k={request.top_k}")
        
        # Perform search
        results = controller.search_documents(
            query=request.query,
            collection_name=request.collection_name,
            top_k=request.top_k
        )
        
        logger.info(f"Search completed: found {len(results)} results")
        
        # Format results
        document_results = [
            DocumentResult(
                content=doc.page_content,
                metadata=doc.metadata,
                score=float(score)
            )
            for doc, score in results
        ]
        
        return SearchResponse(
            status="success",
            query=request.query,
            results=document_results,
            total_results=len(document_results)
        )
        
    except Exception as e:
        logger.error(f"Search failed: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=500,
            detail=f"Search failed: {str(e)}"
        )
