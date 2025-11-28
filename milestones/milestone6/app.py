"""Main application entry point"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import chat_router, history_router
from repositories.database.db_connection import init_db
import logging


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="EBLA RAG Chat API - Milestone 5",
    description="Context-aware RAG system with chat history and prompt engineering",
    version="5.0.0"
)

# Initialize database on startup
@app.on_event("startup")
async def startup_event():
    logger.info("Initializing database...")
    init_db()
    logger.info("Database initialized successfully")


# Include routers
app.include_router(chat_router.router)
app.include_router(history_router.router)

@app.get("/")
async def root():
    return {
        "message": "EBLA RAG Chat API - Milestone 5",
        "endpoints": {
            "chat": "/api/v1/chat",
            "history": "/api/v1/history/{session_id}",
            "docs": "/docs"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
