"""Pydantic schemas for API request/response validation."""

from pydantic import BaseModel, Field,ConfigDict
from typing import List, Dict, Any


class ChatRequest(BaseModel):
    """Request model for chat endpoint."""
    query: str = Field(..., description="User's question")
    collection_name: str = Field(default="documents", description="ChromaDB collection name")
    top_k: int = Field(default=3, ge=1, le=10, description="Number of context documents to retrieve")
    
    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "query": "What services does EBLA provide?",
                "collection_name": "documents",
                "top_k": 3
            }
        }
    )

class SourceDocument(BaseModel):
    """Source document model."""
    content: str = Field(..., description="Document content")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Document metadata")
    score: float = Field(..., description="Similarity score")
    
    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "content": "EBLA supports the following infrastructure services...",
                "metadata": {"source": "data/ebla_services.txt"},
                "score": 1.69
            }
        }
    )

class ChatResponse(BaseModel):
    """Response model for chat endpoint."""
    status: str = Field(..., description="Operation status")
    query: str = Field(..., description="Original query")
    answer: str = Field(..., description="Generated answer")
    sources: List[SourceDocument] = Field(..., description="Source documents used for context")
    
    model_config = ConfigDict(
        json_schema_extra = {
            "example": {
                "status": "success",
                "query": "What services does EBLA provide?",
                "answer": "EBLA provides infrastructure services including Microsoft-based Infrastructure...",
                "sources": [
                    {
                        "content": "EBLA supports the following infrastructure services...",
                        "metadata": {"source": "data/ebla_services.txt"},
                        "score": 1.69
                    }
                ]
            }
        }
    )
