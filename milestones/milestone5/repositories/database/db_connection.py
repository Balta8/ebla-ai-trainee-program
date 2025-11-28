"""Database connection management using SQLAlchemy."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models.base import Base
from config import settings
from typing import Generator


# Create engine and session factory at module level
engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def init_db() -> None:
    """Initialize the database by creating all tables."""
    Base.metadata.create_all(bind=engine)


def get_db() -> Generator[Session, None, None]:
    """
    Dependency function for FastAPI endpoints.
    Provides a database session and ensures it's closed after use.
    
    Yields:
        Session: SQLAlchemy Session object connected to the database.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
