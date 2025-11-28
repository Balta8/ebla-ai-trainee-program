"""Repository for Summary-related database operations."""

from sqlalchemy.orm import Session as DBSession_Type
from models.summary import SummaryModel
from typing import List, Optional


class SummaryRepository:
    """Handles all database operations for conversation summaries."""
    
    def __init__(self, db: DBSession_Type):
        self.db = db

    def create_summary(
        self, 
        session_id: str, 
        summary_text: str,
        start_message_id: Optional[str] = None,
        end_message_id: Optional[str] = None
    ) -> str:
        """
        Creates a summary for a range of messages in a session.
        
        Args:
            session_id: The session ID
            summary_text: The generated summary text
            start_message_id: Optional ID of first message in range
            end_message_id: Optional ID of last message in range
            
        Returns:
            The created summary ID
        """
        try:
            new_summary = SummaryModel(
                session_id=session_id,
                summary_text=summary_text,
                start_message_id=start_message_id,
                end_message_id=end_message_id
            )
            self.db.add(new_summary)
            self.db.commit()
            self.db.refresh(new_summary)
            return new_summary.summary_id
        except Exception as e:
            self.db.rollback()
            raise e

    def get_summaries_by_session(self, session_id: str) -> List[SummaryModel]:
        """
        Retrieves all summaries for a session.
        
        Args:
            session_id: The session ID
            
        Returns:
            List of Summary ORM objects
        """
        try:
            return self.db.query(SummaryModel).filter(
                SummaryModel.session_id == session_id
            ).order_by(SummaryModel.created_date.asc()).all()
        except Exception as e:
            raise ValueError(f"Error fetching summaries: {e}")

    def get_latest_summary(self, session_id: str) -> Optional[SummaryModel]:
        """
        Retrieves the most recent summary for a session.
        
        Args:
            session_id: The session ID
            
        Returns:
            The latest Summary object, or None if no summaries exist
        """
        try:
            return self.db.query(SummaryModel).filter(
                SummaryModel.session_id == session_id
            ).order_by(SummaryModel.created_date.desc()).first()
        except Exception as e:
            raise ValueError(f"Error fetching latest summary: {e}")
