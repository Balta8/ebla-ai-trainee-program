"""Session model definition for chat history database."""

from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base, generate_uuid

class SessionModel(Base):
    """
    Session model representing a chat session in the chat history database.

    Attributes:
        session_id (str): Unique identifier for the session.
        user_id (str): Identifier for the user associated with the session.
        created_date (datetime): Timestamp when the session was created.
    """
    __tablename__ = "sessions"

    session_id: str = Column(String(255), primary_key=True, default=generate_uuid)
    user_id: str = Column(String(255), ForeignKey("users.user_id"), nullable=False)
    created_date: datetime = Column(DateTime, default=datetime.utcnow)

    # Relationship 
    user = relationship("UserModel", back_populates="sessions")

    # cascade="all, delete-orphan":
    # - "all": apply all operations (save/delete) on Session to its Messages.
    # - "delete-orphan": automatically delete messages that no longer belong to any session.
    messages = relationship("MessageModel", back_populates="session", cascade="all, delete-orphan")
    summaries = relationship("SummaryModel", back_populates="session")
