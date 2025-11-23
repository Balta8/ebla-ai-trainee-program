"""Chat router for RAG endpoint."""

from fastapi import APIRouter, HTTPException
from models.api_schemas import ChatRequest, ChatResponse
from controllers.rag_controller import RAGController
import logging

logger = logging.getLogger(__name__)
router = APIRouter()
controller = RAGController()


@router.post("/chat", response_model=ChatResponse, tags=["Chat"])
async def chat_endpoint(request: ChatRequest):
    """Chat with the RAG system."""
    try:
        logger.info(f"Chat request: query='{request.query}'")
        return controller.answer_question(request)
        
    except Exception as e:
        logger.error(f"Chat failed: {str(e)}", exc_info=True)
        raise HTTPException(status_code=500, detail=f"Chat failed: {str(e)}")
