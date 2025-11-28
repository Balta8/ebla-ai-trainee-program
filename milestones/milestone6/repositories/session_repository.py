"""Repository for Session-related database operations."""

from sqlalchemy.orm import Session as DBSession_Type
from models.session import SessionModel as DBSession
from typing import Optional


class SessionRepository:
    """Handles all database operations for chat sessions."""
    
    def __init__(self, db: DBSession_Type):
        self.db = db

    def create_session(self, user_id: Optional[str] = None) -> str:
        """
        Creates a new chat session.
        
        Args:
            user_id: Optional user ID to associate with session
            
        Returns:
            The created session ID
        """
        try:
            new_session = DBSession(user_id=user_id)
            self.db.add(new_session)
            self.db.commit()
            self.db.refresh(new_session)
            return new_session.session_id

        except Exception as e:
            # Rollback to keep session clean if commit fails
            self.db.rollback()
            # Raise the error so the caller knows something went wrong
            raise e
        

    def get_session(self, session_id: str) -> Optional[DBSession]:
        """
        Retrieves a session by ID.
        
        Args:
            session_id: The session ID to look up
            
        Returns:
            The session object if found, None otherwise
        """
        try:
            return self.db.query(DBSession).filter(
                DBSession.session_id == session_id
            ).first()
        except Exception as e:
            raise ValueError(f"Error fetching session: {e}")
        

    def session_exists(self, session_id: str) -> bool:
        """
        Checks if a session exists.
        
        Args:
            session_id: The session ID to check
            
        Returns:
            True if session exists, False otherwise
        """
        try:
            return self.get_session(session_id) is not None
        except Exception as e:
            raise ValueError(f"Error checking session existence: {e}")

