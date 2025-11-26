"""Database connection management using SQLAlchemy."""

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from models.base import Base
from dotenv import load_dotenv
import os
from typing import Generator

# Load environment variables from .env file

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in .env file")

class DatabaseManager:
    """Database connection and session management for SQL Server."""

    engine: Engine
    SessionLocal: sessionmaker

    def __init__(self, database_url: str = DATABASE_URL, autocommit: bool = False, autoflush: bool = False) -> None:
        """
        Initialize the DatabaseManager with a SQLAlchemy engine and session factory.

        Args:
            database_url (str): Database connection URL.
            autocommit (bool): If False, sessions require explicit commit() to save changes.
            autoflush (bool): If False, changes are not automatically flushed to the database.
        """
        self.engine = create_engine(database_url)
        self.SessionLocal = sessionmaker(autocommit=autocommit, autoflush=autoflush, bind=self.engine)


    def init_db(self) -> None:
        """Initialize the database by creating all tables."""
        Base.metadata.create_all(bind=self.engine)

    def get_db(self) -> Generator[Session, None, None]:
        """
        Provide a database session for FastAPI endpoints.

        This function is a generator that yields a Session object and ensures
        the session is closed after use.

        Yields:
            Session: SQLAlchemy Session object connected to the database.
        """
        db: Session = self.SessionLocal()
        try:
            yield db
        finally:
            db.close()


