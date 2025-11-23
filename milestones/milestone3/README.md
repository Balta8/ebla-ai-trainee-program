# Milestone 3: Data Preparation & Indexing

A complete REST API for document indexing and semantic search using **LangChain**, **ChromaDB**, and **FastAPI**. This system allows you to index text documents (PDF & TXT) and perform semantic searches without LLM generation - pure retrieval only.

## ✅ Key Deliverables

This milestone successfully implements the following requirements:

- [x] **Preprocess text data, create embeddings, and index documents**: Implemented using LangChain `RecursiveCharacterTextSplitter` and HuggingFace Embeddings.
- [x] **Expose operations via FastAPI endpoints**: Created a full FastAPI application with routers for modularity.
- [x] **Prepare dataset**: Included sample EBLA services documents (PDF & TXT) in `data/`.
- [x] **Generate embeddings using a vector store**: Integrated **ChromaDB** for persistent vector storage.
- [x] **Build a FastAPI service with endpoints**:
  - `POST /api/v1/index`: Preprocesses and indexes documents.
  - `POST /api/v1/search`: Accepts a query and returns relevant documents.
- [x] **Clean Architecture**: Refactored to separate concerns (Router, Controller, Service, Utils).

## 📁 Project Structure

```
milestone3/
├── app.py                    # FastAPI application entry point
├── main.py                   # CLI entry point (optional)
├── requirements.txt          # Project dependencies
├── .gitignore                # Git ignore rules
├── routers/                  # HTTP Route Handlers (Thin Layer)
│   ├── index.py              # Indexing endpoint 
│   └── search.py             # Search endpoint 
├── controllers/              # Orchestration Layer
│   └── document_controller.py # Coordinates indexing and search
├── services/                 # Business Logic Layer
│   ├── document_service.py   # Business logic for document ops
│   └── vector_store.py       # Vector Store operations (Stateful)
├── utils/                    # Helper Functions (Stateless)
│   ├── document_loader.py    # Document loading (PDF/TXT)
│   ├── text_processor.py     # Text chunking
│   ├── file_utils.py         # Path resolution utilities
│   └── logging_config.py     # Logging configuration
├── models/                   # Data Models
│   └── api_schemas.py        # Pydantic request/response models
├── views/                    # Presentation Layer
│   ├── base_view.py          # Abstract base class
│   └── cli_view.py           # CLI presentation layer
├── data/                     # Document dataset (PDFs & TXTs)
```

## 🔍 How It Works

1. **Document Loading**:
   - Load all `(PDF, TXT)` files from specified directory
   - Create LangChain Document objects with metadata

2. **Text Processing**:
   - Split documents into chunks (500 chars, 50 overlap)
   - Preserve context with overlapping text

3. **Vector Store Creation**:
   - Generate embeddings using HuggingFace model (`sentence-transformers/all-MiniLM-L6-v2`)
   - Store in ChromaDB with automatic persistence

4. **Semantic Search**:
   - Convert query to embedding
   - Find most similar document chunks
   - Return results with similarity scores

## � Installation & Setup

### 1. Create Virtual Environment

```bash
cd milestones/milestone3
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Note**: This project uses:
- **ChromaDB 1.3.5+** (compatible with NumPy 2.0+)
- **Python 3.13** compatible packages
- **LangChain 0.3+** with latest community packages

### 3. Verify Installation

```bash
python -c "import chromadb; import langchain; print('✅ All dependencies installed successfully!')"
```

## 🔧 Usage

### Option 1: Run API Server

```bash
# Make sure you're in the milestone3 directory with venv activated
source venv/bin/activate
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
  
### Option 2: Run CLI (Optional)

```bash
python main.py
```

## 📡 API Endpoints

### 1. Index Documents
**POST** `/api/v1/index`

Indexes documents from the specified directory.

**Request Body**:
```json
{
  "documents_path": "data",
  "collection_name": "documents",
  "chunk_size": 500,
  "chunk_overlap": 50
}
```

**Response**:
```json
{
  "status": "success",
  "message": "Documents indexed successfully",
  "documents_indexed": 11,
  "chunks_created": 22,
  "collection_name": "documents"
}
```

**cURL Example**:
```bash
curl -X POST "http://localhost:8000/api/v1/index" \
  -H "Content-Type: application/json" \
  -d '{
    "documents_path": "data",
    "collection_name": "documents",
    "chunk_size": 500,
    "chunk_overlap": 50
  }'
```

### 2. Search Documents
**POST** `/api/v1/search`

Performs semantic search on indexed documents.

**Request Body**:
```json
{
  "query": "What services does EBLA provide?",
  "collection_name": "documents",
  "top_k": 3
}
```

**Response**:
```json
{
  "status": "success",
  "query": "What services does EBLA provide?",
  "results": [
    {
      "content": "EBLA supports the following infrastructure services: Microsoft-based Infrastructure...",
      "metadata": {
        "source": "data/ebla_services.txt",
        "chunk_index": 4
      },
      "score": 0.45
    },
    {
      "content": "Professional Services: Ebla's professional services ensure end-to-end solutions...",
      "metadata": {
        "source": "data/ebla_services.txt",
        "chunk_index": 5
      },
      "score": 0.52
    }
  ],
  "total_results": 2
}
```

**cURL Example**:
```bash
curl -X POST "http://localhost:8000/api/v1/search" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What services does EBLA provide?",
    "collection_name": "documents",
    "top_k": 3
  }'
```

## 🏗️ Architecture & Tech Stack

### Technologies
- **FastAPI**: High-performance web framework for building APIs
- **LangChain 0.3+**: Framework for developing applications powered by language models
- **ChromaDB 1.3.5+**: AI-native open-source embedding database
- **HuggingFace**: Used for `sentence-transformers/all-MiniLM-L6-v2` embeddings
- **Pydantic 2.5+**: Data validation using Python type hints
- **Uvicorn**: ASGI server for production deployment

### Architecture Pattern
This project follows **Clean Architecture** principles:

```
┌─────────────┐
│   Routers   │  ← HTTP Layer (FastAPI routes)
└──────┬──────┘
       │
┌──────▼──────┐
│ Controllers │  ← Orchestration Layer
└──────┬──────┘
       │
┌──────▼──────┐
│  Services   │  ← Business Logic Layer
└──────┬──────┘
       │
┌──────▼──────┐
│    Utils    │  ← Helper Functions (Stateless)
└─────────────┘
```

**Benefits**:
- ✅ **Separation of Concerns**: Each layer has a single responsibility
- ✅ **Testability**: Easy to unit test each layer independently
- ✅ **Maintainability**: Changes in one layer don't affect others
- ✅ **Reusability**: Services and utils can be reused across different controllers

## 🔧 Configuration

### Environment Variables (Optional)
Create a `.env` file for custom configuration:

```env
CHROMA_DB_PATH=./chroma_db
LOG_LEVEL=INFO
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Customization
- **Chunk Size**: Adjust in the index request (default: 500)
- **Chunk Overlap**: Adjust in the index request (default: 50)
- **Embedding Model**: Change in `services/vector_store.py`
- **Collection Name**: Specify different collections for different datasets

## 📝 Logging

Logs are automatically saved to `logs/app_YYYYMMDD_HHMMSS.log` with the following format:
```
2025-11-23 07:35:07 - root - INFO - Application startup complete
```

## 🐛 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'langchain_huggingface'`
**Solution**: Make sure you're using the virtual environment:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: `AttributeError: np.float_ was removed in NumPy 2.0`
**Solution**: This is fixed in ChromaDB 1.3.5+. Update your dependencies:
```bash
pip install -U chromadb
```

### Issue: Port 8000 already in use
**Solution**: Kill the existing process or use a different port:
```bash
lsof -i :8000  # Find the process
kill -9 <PID>  # Kill it
# Or use a different port:
uvicorn app:app --reload --port 8001
```

