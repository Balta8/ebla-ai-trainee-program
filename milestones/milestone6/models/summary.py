"""Summary model definition for chat history database."""

from sqlalchemy import Column, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base, generate_uuid

class SummaryModel(Base):
    """
    Summary model representing a chat session summary in the chat history database.

    Attributes:
        summary_id (str): Unique identifier for the summary.
        session_id (str): Identifier for the session associated with the summary.
        summary_text (str): Text content of the summary.
        start_message_id (str | None): ID of the first message included in the summary.
        end_message_id (str | None): ID of the last message included in the summary.
        created_date (datetime): Timestamp when the summary was created.
    """
    __tablename__ = "summaries"

    summary_id: str = Column(String(255), primary_key=True, default=generate_uuid)
    session_id: str = Column(String(255), ForeignKey("sessions.session_id"), nullable=False)
    summary_text: str = Column(Text, nullable=False)
    start_message_id: str | None = Column(String(255), ForeignKey("messages.message_id"), nullable=True)
    end_message_id: str | None = Column(String(255), ForeignKey("messages.message_id"), nullable=True)
    created_date: datetime = Column(DateTime, default=datetime.utcnow)

    # Relationship with session
    session = relationship("SessionModel", back_populates="summaries")
