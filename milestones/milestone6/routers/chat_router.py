""" Chat Router for RAG-based context-aware chat endpoint."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services.rag_service import RAGService
from schemas.chat_schema import ChatRequest, ChatResponse
from repositories.database.db_connection import get_db

router = APIRouter(
    prefix="/api/v1/chat",
    tags=["chat"]
)

@router.post("", response_model=ChatResponse)
async def chat(request: ChatRequest, db: Session = Depends(get_db)):
    """
    Context-aware RAG chat endpoint with history.
    
    - Creates a new session if session_id is not provided
    - Retrieves chat history for context
    - Performs vector search for relevant documents
    - Generates AI response using LLM
    - Saves conversation to database
    """
    rag_service = RAGService(db)
    
    try:
        response = rag_service.process_chat(request)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

    return response

