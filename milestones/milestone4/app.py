"""FastAPI application for RAG system."""

from fastapi import FastAPI
from routers.chat import router as chat_router
from utils.logging_config import setup_logging
import logging

# Setup logging
setup_logging(log_level=logging.INFO, log_to_file=True)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="RAG Chat API",
    description="""
    A Retrieval-Augmented Generation (RAG) API using LangChain, ChromaDB, and Ollama.
    
    ## Features
    * **Semantic Search**: Retrieve relevant documents
    * **LLM Generation**: Generate grounded answers using Qwen2.5
    * **Context Awareness**: Uses retrieved documents as context
    """,
    version="1.0.0"
)

# Include routers
app.include_router(chat_router, prefix="/api/v1")

logger.info("RAG API initialized")


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint."""
    return {
        "message": "RAG Chat API",
        "version": "1.0.0",
        "docs": "/docs"
    }
