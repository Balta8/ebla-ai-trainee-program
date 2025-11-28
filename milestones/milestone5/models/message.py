"""Message model definition for chat history database."""

from sqlalchemy import Column, String, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base, generate_uuid

class MessageModel(Base):
    """
    Message model representing a chat message in the chat history database.

    Attributes:
        message_id (str): Unique identifier for the message.
        session_id (str): Identifier for the session associated with the message.
        role (str): Role of the message sender (e.g., 'user' or 'bot').
        content (str): Content of the message.
        created_date (datetime): Timestamp when the message was created.
    """
    __tablename__ = "messages"

    message_id : str = Column(String(255), primary_key=True, default=generate_uuid)
    session_id : str = Column(String(255), ForeignKey("sessions.session_id"), nullable=False)
    role : str = Column(String(50), nullable=False)
    content : str = Column(Text, nullable=False)
    created_date : datetime = Column(DateTime, default=datetime.utcnow)

    # Relationship with session
    session = relationship("SessionModel", back_populates="messages")