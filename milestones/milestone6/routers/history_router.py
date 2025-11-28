""" History Router for retrieving session chat history. """

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas.history_schema import SessionHistoryResponse
from repositories.database.db_connection import get_db
from services.history_service import HistoryService

router = APIRouter(
    prefix="/api/v1/history",
    tags=["history"]
)

@router.get("/{session_id}", response_model=SessionHistoryResponse)
async def get_session_history(session_id: str, db: Session = Depends(get_db)):
    """
    Retrieve the chat history for a specific session.
    """
    service = HistoryService(db)
    try:
        response = service.fetch_session_history(session_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return response
