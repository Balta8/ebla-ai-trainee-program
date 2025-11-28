"""Application configuration management using Pydantic Settings."""

import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from typing import Optional

# Explicitly load .env file from the same directory as this config file
env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Database Configuration
    database_url: str
    
    # LLM Configuration
    llm_model_name: str = "qwen2.5:7b"
    llm_base_url: str = "http://localhost:11434"
    llm_temperature: float = 0.7
    
    # Vector Store Configuration
    vector_store_persist_dir: str = "./chroma_db"
    embedding_model_name: str = "sentence-transformers/all-MiniLM-L6-v2"
    
    # RAG Configuration
    chat_history_limit: int = 5
    default_top_k: int = 3
    default_collection_name: str = "documents"
    
    # Text Processing Configuration
    chunk_size: int = 500
    chunk_overlap: int = 50

    # Maximum Messages to Summaries
    summary_max_messages: int = 50
    
    class Config:
        case_sensitive = False
        extra = "ignore"


# Singleton instance
settings = Settings()
