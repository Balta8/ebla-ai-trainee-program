# services/history_service.py
from sqlalchemy.orm import Session
from repositories.session_repository import SessionRepository
from repositories.message_repository import MessageRepository
from schemas.history_schema import SessionHistoryResponse

class HistoryService:
    """Service layer for chat history operations."""

    def __init__(self, db: Session):
        self.session_repo = SessionRepository(db)
        self.message_repo = MessageRepository(db)

    def fetch_session_history(self, session_id: str) -> SessionHistoryResponse:
        """
        Fetch the chat history for a given session ID and return full Pydantic response.
        
        Raises:
            ValueError: if session does not exist
        """
        if not self.session_repo.session_exists(session_id):
            raise ValueError(f"Session {session_id} not found")

        messages = self.message_repo.get_messages_by_session(session_id)
        message_schemas = self.message_repo.convert_to_schemas(messages)

        return SessionHistoryResponse(
            session_id=session_id,
            messages=message_schemas
        )

