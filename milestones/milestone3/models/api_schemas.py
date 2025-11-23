"""Pydantic schemas for API request/response validation."""

from pydantic import BaseModel, Field
from typing import List, Optional

# INDEX ENDPOINT SCHEMAS

class IndexRequest(BaseModel):
    """Request model for document indexing."""
    documents_path: str = Field(..., description="Path to documents directory")
    collection_name: str = Field(default="documents", description="ChromaDB collection name")
    chunk_size: int = Field(default=500, ge=100, le=2000, description="Size of text chunks")
    chunk_overlap: int = Field(default=50, ge=0, le=500, description="Overlap between chunks")
    
    class Config:
        json_schema_extra = {
            "example": {
                "documents_path": "data",
                "collection_name": "documents",
                "chunk_size": 500,
                "chunk_overlap": 50
            }
        }


class IndexResponse(BaseModel):
    """Response model for document indexing."""
    status: str = Field(..., description="Operation status")
    message: str = Field(..., description="Status message")
    documents_indexed: int = Field(..., description="Number of documents indexed")
    chunks_created: int = Field(..., description="Number of text chunks created")
    collection_name: str = Field(..., description="ChromaDB collection name")
    
    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "message": "Documents indexed successfully",
                "documents_indexed": 11,
                "chunks_created": 22,
                "collection_name": "documents"
            }
        }

# SEARCH ENDPOINT SCHEMAS

class SearchRequest(BaseModel):
    """Request model for document search."""
    query: str = Field(..., description="Search query text")
    collection_name: str = Field(default="documents", description="ChromaDB collection name")
    top_k: int = Field(default=3, ge=1, le=20, description="Number of results to return")
    
    class Config:
        json_schema_extra = {
            "example": {
                "query": "What services does EBLA provide?",
                "collection_name": "documents",
                "top_k": 3
            }
        }

class DocumentResult(BaseModel):
    """Single document search result."""
    content: str = Field(..., description="Document text content")
    metadata: dict = Field(default_factory=dict, description="Document metadata")
    score: Optional[float] = Field(None, description="Similarity score")
    
    class Config:
        json_schema_extra = {
            "example": {
                "content": "EBLA is a leading technology company specializing in educational technology solutions...",
                "metadata": {"source": "data/ebla_overview.txt", "chunk_index": 0},
                "score": 1.65
            }
        }


class SearchResponse(BaseModel):
    """Response model for document search."""
    status: str = Field(..., description="Operation status")
    query: str = Field(..., description="Original search query")
    results: List[DocumentResult] = Field(..., description="Search results")
    total_results: int = Field(..., description="Number of results returned")
    
    class Config:
        json_schema_extra = {
            "example": {
                "status": "success",
                "query": "What services does EBLA provide?",
                "results": [
                    {
                        "content": "EBLA supports the following infrastructure services: Microsoft-based Infrastructure, Cloud Services (AWS, Azure, Google Cloud)...",
                        "metadata": {"source": "data/ebla_services.txt", "chunk_index": 4},
                        "score": 1.69
                    }
                ],
                "total_results": 3
            }
        }
