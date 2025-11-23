# Milestone 4: Retrieval & LLM Integration

A complete **Retrieval-Augmented Generation (RAG)** system that combines semantic search with local LLM generation using **ChromaDB**, **LangChain**, and **Ollama**.

## 🎯 Objective

Integrate the document retrieval system (Milestone 3) with a local LLM (Milestone 2) to create a fully functional RAG API that:
1. Retrieves relevant documents based on user queries
2. Uses retrieved context to generate accurate, grounded responses
3. Exposes the functionality via FastAPI endpoints

## ✅ Key Deliverables

- [x] **LLM Integration**: Connect to Ollama (Qwen2.5:7b) for text generation
- [x] **RAG Pipeline**: Combine retrieval + generation in a single workflow
- [x] **Chat Endpoint**: `POST /api/v1/chat` - accepts query, returns AI-generated answer with sources
- [x] **Prompt Engineering**: Design effective prompts for accurate responses
- [x] **Context Management**: Pass retrieved documents to LLM as context
- [x] **Source Attribution**: Return source documents with the answer
- [x] **Clean Architecture**: Implemented Router → Controller → Service → Utils pattern

## 📁 Project Structure

```
milestone4/
├── app.py                    # FastAPI application entry point
├── requirements.txt          # Dependencies
├── routers/                  # HTTP Route Handlers (Thin Layer)
│   └── chat.py               # Chat endpoint definition
├── controllers/              # Orchestration Layer
│   └── rag_controller.py     # Coordinates Retrieval & Generation
├── services/                 # Business Logic Layer
│   ├── rag_service.py        # RAG logic (Prompting, Formatting)
│   └── vector_store.py       # Vector Store operations (Stateful)
├── utils/                    # Helper Functions (Stateless)
│   ├── llm_service.py        # Ollama LLM wrapper
│   ├── document_loader.py    # Document loading utilities
│   └── text_processor.py     # Text chunking utilities
├── models/                   # Data Models
│   └── api_schemas.py        # Pydantic schemas for Request/Response
├── views/                    # Presentation Layer
│   ├── base_view.py          # Abstract Base Class
│   └── cli_view.py           # CLI Output formatting
└── data/                     # Source documents
```

## 🔄 How It Works

1. **User sends a query** via `/api/v1/chat`
2. **Router** receives request and passes it to **Controller**
3. **Controller** uses **VectorStore Service** to retrieve top-k relevant documents
4. **Controller** passes documents + query to **RAG Service**
5. **RAG Service** constructs a prompt and calls **LLM Utility**
6. **LLM generates** an answer based on the context
7. **System returns** the answer + source documents

## 🛠️ Tech Stack

- **FastAPI**: REST API framework
- **LangChain 0.3+**: RAG orchestration
- **ChromaDB 1.3.5+**: Vector database (NumPy 2.0+ compatible)
- **Ollama**: Local LLM runtime (Qwen2.5:7b)
- **HuggingFace**: Embeddings (sentence-transformers/all-MiniLM-L6-v2)
- **Pydantic 2.5+**: Data validation

## � Installation & Setup

### 1. Install Ollama

**macOS:**
```bash
brew install ollama

# Start Ollama service
ollama serve
```

**Linux:**
```bash
curl -fsSL https://ollama.com/install.sh | sh
ollama serve
```

### 2. Pull the Qwen2.5 Model

```bash
ollama pull qwen2.5:7b
```

Verify installation:
```bash
ollama list
```

### 3. Create Virtual Environment

```bash
cd milestones/milestone4
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 4. Install Python Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Note**: This project uses:
- **ChromaDB 1.3.5+** (compatible with NumPy 2.0+)
- **Python 3.13** compatible packages
- **LangChain 0.3+** with latest community packages

### 5. Verify Installation

```bash
python -c "import chromadb; import langchain; import ollama; print('✅ All dependencies installed successfully!')"
```

## � Usage

### Option 1: Run API Server

```bash
# Make sure you're in the milestone4 directory with venv activated
source venv/bin/activate
uvicorn app:app --reload --host 0.0.0.0 --port 8001
```

- **Swagger UI**: [http://localhost:8001/docs](http://localhost:8001/docs)
- **ReDoc**: [http://localhost:8001/redoc](http://localhost:8001/redoc)

### Option 2: Test with cURL

First, make sure you have indexed documents (from milestone3 or run indexing endpoint).

**Chat Request:**
```bash
curl -X POST "http://localhost:8001/api/v1/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What services does EBLA provide?",
    "collection_name": "documents",
    "top_k": 3
  }'
```

## 📡 API Endpoint

### POST `/api/v1/chat`

Performs RAG: retrieves relevant documents and generates an answer using LLM.

**Request Body:**
```json
{
  "query": "What services does EBLA provide?",
  "collection_name": "documents",
  "top_k": 3
}
```

**Parameters:**
- `query` (string, required): User's question
- `collection_name` (string, optional): ChromaDB collection name (default: "documents")
- `top_k` (integer, optional): Number of documents to retrieve (default: 3)

**Response:**
```json
{
  "status": "success",
  "query": "What services does EBLA provide?",
  "answer": "EBLA provides infrastructure services including Microsoft-based Infrastructure, Cloud Services (AWS, Azure, Google Cloud), and educational technology solutions.",
  "sources": [
    {
      "content": "EBLA supports the following infrastructure services...",
      "metadata": {"source": "data/ebla_services.txt"},
      "score": 0.45
    }
  ]
}
```

## 🏗️ Architecture Pattern

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
│  Services   │  ← Business Logic Layer (RAG, VectorStore)
└──────┬──────┘
       │
┌──────▼──────┐
│    Utils    │  ← Helper Functions (LLM, Loaders)
└─────────────┘
```

**Benefits**:
- ✅ **Separation of Concerns**: Each layer has a single responsibility
- ✅ **Testability**: Easy to unit test each layer independently
- ✅ **Maintainability**: Changes in one layer don't affect others
- ✅ **Reusability**: Services and utils can be reused across different controllers

## 🎓 Learning Objectives

- Understand how RAG systems work end-to-end
- Learn to integrate vector search with LLM generation
- Practice prompt engineering for better responses
- Implement context-aware AI systems
- Apply **Clean Architecture** principles (MVC + Services)

## 🐛 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'ollama'`
**Solution**: Make sure you're using the virtual environment:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: `Connection refused` when calling Ollama
**Solution**: Make sure Ollama service is running:
```bash
# Check if Ollama is running
ps aux | grep ollama

# Start Ollama if not running
ollama serve
```

### Issue: `Model 'qwen2.5:7b' not found`
**Solution**: Pull the model first:
```bash
ollama pull qwen2.5:7b
```

### Issue: `AttributeError: np.float_ was removed in NumPy 2.0`
**Solution**: This is fixed in ChromaDB 1.3.5+. Update your dependencies:
```bash
pip install -U chromadb
```

### Issue: Port 8001 already in use
**Solution**: Kill the existing process or use a different port:
```bash
lsof -i :8001  # Find the process
kill -9 <PID>  # Kill it
# Or use a different port:
uvicorn app:app --reload --port 8002
```

## 📝 Configuration

### Environment Variables (Optional)
Create a `.env` file for custom configuration:

```env
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=qwen2.5:7b
CHROMA_DB_PATH=./chroma_db
LOG_LEVEL=INFO
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### Customization
- **LLM Model**: Change in `utils/llm_service.py` or via environment variable
- **Top-K Results**: Adjust in the chat request (default: 3)
- **Embedding Model**: Change in `services/vector_store.py`
- **Collection Name**: Specify different collections for different datasets

## 📚 Comparison with Milestone 3

| Feature | Milestone 3 | Milestone 4 |
|---------|-------------|-------------|
| **Purpose** | Document indexing & search | RAG with LLM generation |
| **Endpoints** | `/index`, `/search` | `/chat` |
| **Output** | Raw document chunks | AI-generated answers |
| **LLM** | ❌ None | ✅ Ollama (Qwen2.5) |
| **Use Case** | Information retrieval | Question answering |

**Status:** ✅ Completed

