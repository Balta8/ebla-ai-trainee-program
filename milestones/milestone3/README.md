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
- [x] **Documentation**: Comprehensive README and Swagger UI (`/docs`) explaining endpoints and usage.

## 🎓 Key Learnings

### 1. FastAPI Routers (`APIRouter`)
- Learned how to structure a large API by splitting endpoints into separate files (`routers/index.py`, `routers/search.py`).
- Used `APIRouter` to modularize the application, making the main `app.py` clean and maintainable.
- Applied prefixes and tags to group related endpoints automatically in Swagger UI.

### 2. Pydantic Schemas (`BaseModel`)
- Moved away from unstructured dictionaries to strict data validation using **Pydantic**.
- Created dedicated schemas (`IndexRequest`, `SearchResponse`, etc.) in `schemas/api_schemas.py`.
- This ensures type safety, automatic validation, and generates accurate API documentation.

### 3. Advanced Logging
- Replaced basic `print()` statements with a professional **Logging** system (`logging` module).
- Configured different log levels (`INFO`, `ERROR`) and output destinations (Console & File).
- Learned how to track application flow and debug errors effectively in a production-like environment.

### 4. MVC Architecture with Dependency Injection
- Successfully adapted the **Model-View-Controller** pattern for a Web API.
- The **Controller** handles logic, **Routers** handle HTTP requests (View layer for API), and **Models** handle data.
- Implemented **Dependency Injection**: The Controller receives a `View` from outside, making it flexible and testable.
- Used **Null Object Pattern** (`SilentView`) to avoid conditional logic when no output is needed (API context).

## 📁 Project Structure

```
milestone3/
├── app.py                    # FastAPI application entry point
├── main.py                   # CLI application entry point
├── requirements.txt          # Project dependencies
├── data/                     # Document dataset (PDFs & TXTs)
├── logs/                     # Application logs (auto-generated)
├── chroma_db/                # Vector database storage (auto-generated)
├── controllers/
│   └── document_controller.py # logic orchestration
├── models/
│   ├── document_loader.py    # Document loading (PDF/TXT)
│   ├── text_processor.py     # Text chunking 
│   └── vector_store.py       # ChromaDB management
├── routers/
│   ├── index.py              # Indexing endpoint 
│   └── search.py             # Search endpoint 
├── schemas/
│   └── api_schemas.py        # Pydantic request/response models
├── utils/
│   └── logging_config.py     # Logging configuration
└── views/
    ├── base_view.py          # Abstract base class & SilentView
    └── cli_view.py           # CLI presentation layer
```
## 🔍 How It Works

1. **Document Loading**:
   - Load all `(PDF, TXT)` files from specified directory
   - Create LangChain Document objects with metadata

2. **Text Processing**:
   - Split documents into chunks (500 chars, 50 overlap)
   - Preserve context with overlapping text
   - Add chunk indices to metadata

3. **Vector Store Creation**:
   - Generate embeddings using HuggingFace model
   - Store in ChromaDB with automatic persistence
   - Support multiple collections

4. **Semantic Search**:
   - Convert query to embedding
   - Find most similar document chunks
   - Return results with similarity scores

## � Installation & Setup

1. **Activate Virtual Environment**:
   ```bash
   # Assuming you are in the project root
   source venv/bin/activate
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r milestones/milestone3/requirements.txt
   ```

## 🔧 Usage

### Option 1: REST API (Recommended)

Start the server from the `milestone3` directory:

```bash
cd milestones/milestone3
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)

### Option 2: CLI Tool

Run the interactive command-line interface:

```bash
python milestones/milestone3/main.py
```
Follow the menu:
- **1**: Index documents from a directory
- **2**: Search for relevant documents
- **3**: Exit

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
      "score": 1.69
    }
  ],
  "total_results": 1
}
```

## 🏗️ Architecture & Tech Stack

- **FastAPI**: High-performance web framework for building APIs.
- **LangChain**: Framework for developing applications powered by language models.
- **ChromaDB**: AI-native open-source embedding database.
- **HuggingFace**: Used for `sentence-transformers/all-MiniLM-L6-v2` embeddings.
- **Pydantic**: Data validation using Python type hints.
- **Uvicorn**: ASGI web server implementation.




