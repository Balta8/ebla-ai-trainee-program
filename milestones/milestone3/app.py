"""FastAPI application for document indexing and search."""

from fastapi import FastAPI
from routers.index import router as index_router
from routers.search import router as search_router
from utils.logging_config import setup_logging
import logging
import uvicorn


# Setup logging
setup_logging(log_level=logging.INFO, log_to_file=True)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Document Indexing & Search API",
    description="""
    A REST API for document indexing and semantic search using LangChain and ChromaDB.
    
    ## Features
    * **Document Indexing**: Load and index PDF and text documents with automatic chunking
    * **Semantic Search**: Find relevant documents using natural language queries
    * **Vector Storage**: Persistent storage using ChromaDB
    * **Embeddings**: HuggingFace sentence-transformers/all-MiniLM-L6-v2
    
    ## Endpoints
    * `POST /api/v1/index` - Index documents from a directory
    * `POST /api/v1/search` - Search for relevant documents
    
    ## Tech Stack
    * FastAPI
    * LangChain
    * ChromaDB
    * HuggingFace Transformers
    """,
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Include routers with prefix
app.include_router(index_router, prefix="/api/v1")
app.include_router(search_router, prefix="/api/v1")

logger.info("FastAPI application initialized")


@app.on_event("startup")
async def startup_event():
    """Run on application startup."""
    logger.info("Application startup complete")


@app.on_event("shutdown")
async def shutdown_event():
    """Run on application shutdown."""
    logger.info("Application shutting down")


@app.get("/", tags=["Root"])
async def root():
    """Root endpoint with API information."""
    return {
        "message": "Document Indexing & Search API",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "index": "POST /api/v1/index",
            "search": "POST /api/v1/search",
            "health": "GET /health"
        }
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "service": "document-search-api",
        "version": "1.0.0"
    }


#if __name__ == "__main__":
#    logger.info("Starting uvicorn server on http://0.0.0.0:8000")
#    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")