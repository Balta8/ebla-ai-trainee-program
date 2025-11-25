"""Chat router for RAG endpoint."""

from fastapi import APIRouter, HTTPException
from models.api_schemas import ChatRequest, ChatResponse
from services.rag_service import RAGService
import logging

logger = logging.getLogger(__name__)
router = APIRouter()

# Initialize RAG service 
rag_service = RAGService()


@router.post("/chat", response_model=ChatResponse, tags=["Chat"])
async def chat_endpoint(request: ChatRequest):
    """
    Chat with the RAG system.
    
    This endpoint:
    1. Retrieves relevant documents from vector store
    2. Generates answer using LLM with context
    3. Returns answer with source documents
    """
    try:
        logger.info(f"Chat request: query='{request.query}'")
        response = rag_service.process_query(request)
        return response
        
    except Exception as e:
        logger.error(f"Chat failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Chat failed: {str(e)}")
