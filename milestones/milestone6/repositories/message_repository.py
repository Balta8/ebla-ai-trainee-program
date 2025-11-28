"""Repository for Message-related database operations."""

from sqlalchemy.orm import Session as DBSession_Type
from models.message import MessageModel
from schemas.history_schema import MessageSchema
from typing import List


class MessageRepository:
    """Handles all database operations for chat messages."""
    
    def __init__(self, db: DBSession_Type):
        self.db = db

    def add_message(self, session_id: str, role: str, content: str) -> str:
        """
        Adds a message to a session.
        
        Args:
            session_id: The session to add the message to
            role: 'user' or 'assistant'
            content: The message content
            
        Returns:
            The created message ID
        """
        try:
            new_message = MessageModel(
                session_id=session_id,
                role=role,
                content=content
            )
            self.db.add(new_message)
            self.db.commit()
            self.db.refresh(new_message)

            return new_message.message_id

        except Exception as e:
            # Rollback in case of error
            self.db.rollback()
            raise e
        
    def get_messages_by_session(self, session_id: str) -> List[MessageModel]:
        """
        Retrieves all messages for a session, ordered chronologically (oldest first).

        Args:
            session_id: The session ID to retrieve messages for

        Returns:
            List of Message ORM objects
        """
        try:
            return (
                self.db.query(MessageModel)
                .filter(MessageModel.session_id == session_id)
                .order_by(MessageModel.created_date.asc())  # oldest first
                .all()
            )
        except Exception as e:
            self.db.rollback()
            raise e


    def get_recent_messages(self, session_id: str, limit: int = 5) -> List[MessageModel]:
        """
        Retrieves the most recent N messages for a session.
        
        Args:
            session_id: The session ID
            limit: Number of recent messages to retrieve
            
        Returns:
            List of Message ORM objects (most recent first)
        """
        try:
            return (
                self.db.query(MessageModel)
                .filter(MessageModel.session_id == session_id)
                .order_by(MessageModel.created_date.desc())
                .limit(limit)
                .all()
            )
        except Exception as e:
            self.db.rollback()
            raise e


    def convert_to_schemas(self, messages: List[MessageModel]) -> List[MessageSchema]:
        """
        Converts ORM Message objects to Pydantic MessageSchema objects.
        
        Args:
            messages: List of ORM Message objects
            
        Returns:
            List of MessageSchema Pydantic objects
        """
        try:
            return [
                MessageSchema(
                    message_id=msg.message_id,
                    role=msg.role,
                    content=msg.content,
                    created_at=msg.created_date
                )
                for msg in messages
            ]
        except Exception as e:
            raise ValueError(f"Error converting ORM messages to schemas: {e}")
