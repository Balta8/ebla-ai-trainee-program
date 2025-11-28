"""User model definition for chat history database."""

from sqlalchemy import Column,String,DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base, generate_uuid

class UserModel(Base):
    """
    User model representing a user in the chat history database.

    Attributes:
        user_id (str): Unique identifier for the user.
        user_name (str): Name of the user.
        created_date (datetime): Timestamp when the user was created.
    """
    __tablename__ = "users"

    user_id: str = Column(String(255), primary_key=True, default=generate_uuid)
    user_name: str = Column(String(255), nullable=False)
    created_date: datetime = Column(DateTime, default=datetime.utcnow)

    # Relationship with sessions
    sessions = relationship("SessionModel", back_populates="user")
