# Milestone 6: Streamlit UI for Milestone 5 RAG System

This is **the same project as Milestone 5** (Context-Aware RAG System) with an added **Streamlit chat UI** that shows:
- Chat messages (user & assistant)
- Current session info
- Retrieved documents side by side

---

## �️ UI Screenshot

![Streamlit Chat UI](docs/Ui_chat.jpeg)

*The Streamlit interface shows the chat on the left and retrieved documents on the right, with the session ID displayed under each assistant response.*

---

All backend logic, database, and API endpoints remain identical to Milestone 5.

---

## 🎯 Milestone Objectives

This milestone focuses on enhancing the RAG system with conversational memory and advanced prompt engineering:

✅ **Understand the importance of chat history and context in conversational AI**  
✅ **Learn the basics of prompt engineering** (instruction design, role prompting, few-shot examples)  
✅ **Design and integrate a chat history storage system**  
✅ **Enhance the existing RAG bot with context-aware conversations**  
✅ **Add summarization of old chat history** (to keep context short but relevant)

---

## 📋 Milestone Requirements & Deliverables

### 1. Chat History & ERD ✅
- [x] **ER Diagram** for chat history with custom table design
- [x] **Database Implementation** using SQLAlchemy ORM with SQL Server
- [x] **Tables**: Users, Sessions, Messages, Summaries
- [x] **Persistence** for user queries, bot responses, and context

### 2. Prompt Engineering ✅
- [x] **Instruction Prompting**: Clear system instructions guide the model
- [x] **Role Prompting**: Assistant persona as "EBLA intelligent assistant"
- [x] **Few-shot Prompting**: Examples in system prompt for consistency
- [x] **Multi-part Prompts**: System + History + Context + Query structure

### 3. Integration with RAG Bot ✅
- [x] **POST /api/v1/chat**: Context-aware chat with RAG + history
- [x] **GET /api/v1/history/{session_id}**: Retrieve stored conversation history
- [x] **Session Management**: Automatic session creation and tracking
- [x] **Context-Aware Responses**: Uses both history and retrieved documents

### 4. Conversation Summarization ✅
- [x] **Automatic Summarization**: Summarizes old chat history when conversations get long
- [x] **Summary Storage**: Summaries saved in database for future reference
- [x] **Context Optimization**: Keeps prompts short while maintaining relevance

---

## 🗄️ Database Schema (ER Diagram)

![ER Diagram](docs/er_diagram.png)

### Database Design

The system uses **4 tables** to manage chat history and context:

#### 1. **Users Table**
Stores user information for multi-user support.

| Column | Type | Description |
|--------|------|-------------|
| `user_id` (PK) | UUID | Unique user identifier |
| `user_name` | String | User's display name |
| `created_date` | DateTime | Account creation timestamp |

#### 2. **Sessions Table**
Represents individual chat conversations.

| Column | Type | Description |
|--------|------|-------------|
| `session_id` (PK) | UUID | Unique session identifier |
| `user_id` (FK) | UUID | Reference to Users table |
| `created_date` | DateTime | Session start timestamp |

**Relationship**: `Users` → `Sessions` (1:N)

#### 3. **Messages Table**
Stores individual messages in conversations.

| Column | Type | Description |
|--------|------|-------------|
| `message_id` (PK) | UUID | Unique message identifier |
| `session_id` (FK) | UUID | Reference to Sessions table |
| `role` | String | "user" or "assistant" |
| `content` | Text | Message content |
| `created_date` | DateTime | Message timestamp |

**Relationship**: `Sessions` → `Messages` (1:N)

#### 4. **Summaries Table**
Stores conversation summaries for long chats.

| Column | Type | Description |
|--------|------|-------------|
| `summary_id` (PK) | UUID | Unique summary identifier |
| `session_id` (FK) | UUID | Reference to Sessions table |
| `summary_text` | Text | Generated summary content |
| `start_message_id` (FK) | UUID | First message in summarized range |
| `end_message_id` (FK) | UUID | Last message in summarized range |
| `created_date` | DateTime | Summary creation timestamp |

**Relationship**: `Sessions` → `Summaries` (1:N)

---

## 📁 Project Structure (Clean Architecture)

```
milestone6/
├── app.py                           # FastAPI application entry point
├── config.py                        # Configuration management 
├── requirements.txt                 # Python dependencies
├── .env                             # Environment variables (database URL, etc.)
├── .gitignore                       # Git ignore rules
├── README.md                        # This file
│
├── docs/                            # Documentation
│   └── er_diagram.png               # ER Diagram image
│   └── PROMPT_ENGINEERING.md        # Demo Documentation
│
├── repositories/                    # Data Access Layer 
│   ├── __init__.py
│   ├── database/                    # Database connection 
│   │   ├── __init__.py
│   │   └── db_connection.py         # SQLAlchemy engine & session management
│   │   
│   ├── session_repository.py        # Session CRUD operations
│   ├── message_repository.py        # Message CRUD operations
│   └── summary_repository.py        # Summary CRUD operations
│
├── models/                          # Database Models (SQLAlchemy ORM)
│   ├── __init__.py
│   ├── base.py                      # Base model class
│   ├── user.py                      # User model
│   ├── session.py                   # Session model
│   ├── message.py                   # Message model
│   └── summary.py                   # Summary model
│
├── schemas/                         # API Contracts (Pydantic)
│   ├── __init__.py
│   ├── chat_schema.py               # Chat request/response schemas
│   └── history_schema.py            # History response schemas
│
├── services/                        # Business Logic Layer
│   ├── __init__.py
│   ├── rag_service.py               # RAG workflow orchestration + summarization
│   ├── history_service.py           # History retrieval service
│   ├── vector_store.py              # ChromaDB vector search
│   ├── llm_service.py               # Ollama LLM client
│   └── document_loader.py           # Document loading utilities
│
├── routers/                         # HTTP Route Handlers
│   ├── __init__.py
│   ├── chat_router.py               # POST /api/v1/chat
│   └── history_router.py            # GET /api/v1/history/{session_id}
│
├── utils/                           # Helper Functions
│   ├── __init__.py
│   ├── text_processor.py            # Text chunking utilities
│   └── prompt_builder.py            # Prompt construction helpers
│
├── test/                            # Test Suite
│   ├── test_session_repo.py         # Session repository tests
│   ├── test_message_repo.py         # Message repository tests
│   ├── test_summary_service.py      # Summarization integration test
│   ├── test_llm_service.py          # LLM service tests
│   ├── test_vector_store.py         # Vector store tests
│   ├── test_document_loader.py      # Document loader tests
│   └── test_text_processor.py       # Text processor tests
│
├── data/                            # Source Documents
│   ├── *.pdf                        # PDF documents for RAG
│   └── *.TXT                        # TXT documents for RAG
│
└── chroma_db/                       # ChromaDB vector store (auto-created)
```

---

## 🔄 System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      HTTP Layer (FastAPI)                    │
│                  Routers: chat_router, history_router        │
└───────────────────────────────┬─────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────┐
│                    Business Logic Layer                      │
│         Services: RAGService, HistoryService, etc.           │
└───────────────────────────────┬─────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────┐
│                    Data Access Layer                         │
│   Repositories: SessionRepo, MessageRepo, SummaryRepo        │
└───────────────────────────────┬─────────────────────────────┘
                                │
┌───────────────────────────────▼─────────────────────────────┐
│                    Database Layer                            │
│          SQLAlchemy ORM + SQL Server Database                │
└─────────────────────────────────────────────────────────────┘
```

**Key Benefits:**
- ✅ **Separation of Concerns**: Each layer has a single responsibility
- ✅ **Testability**: Easy to mock dependencies for unit testing
- ✅ **Maintainability**: Changes in one layer don't affect others
- ✅ **Scalability**: Simple to add new features or swap implementations

---

## 🔄 How It Works (System Flow)

### Chat Flow (POST /api/v1/chat)

```
1. User sends query → Router receives ChatRequest
                      ↓
2. Router → RAGService.process_chat()
                      ↓
3. RAGService orchestrates:
   ├─ Step 1: Create/verify session (SessionRepository)
   ├─ Step 2: Retrieve last 5 messages (MessageRepository)
   ├─ Step 3: Search vector store for relevant docs (VectorStore)
   ├─ Step 4: Build multi-part prompt (System + History + Context + Query)
   ├─ Step 5: Generate answer using LLM (LLMService)
   └─ Step 6: Save user query + AI answer (MessageRepository)
                      ↓
4. Return ChatResponse with answer, sources, and session_id
```

### History Retrieval Flow (GET /api/v1/history/{session_id})

```
1. User requests history → Router receives session_id
                           ↓
2. Router → HistoryService.fetch_session_history()
                           ↓
3. HistoryService:
   ├─ Verify session exists (SessionRepository)
   └─ Retrieve all messages (MessageRepository)
                           ↓
4. Return SessionHistoryResponse with chronological messages
```

### Summarization Flow (Automatic)

```
1. When conversation exceeds 50 messages:
                      ↓
2. RAGService.summarize_session() triggered
                      ↓
3. Summarization process:
   ├─ Retrieve last 50 messages (MessageRepository)
   ├─ Build summarization prompt
   ├─ Generate summary using LLM (LLMService)
   └─ Save summary to database (SummaryRepository)
                      ↓
4. Summary used in future prompts to maintain context
```

---

## 🎓 Prompt Engineering Implementation

### Multi-Part Prompt Structure

The system constructs sophisticated prompts with 4 components:

```python
# 1. System Instructions (Role Prompting)
system_prompt = """
You are an intelligent assistant for EBLA Computer Consultancy.
Your role is to provide accurate, helpful information based on the context provided.
Always be professional, concise, and cite sources when available.
"""

# 2. Chat History (Conversation Context)
history_context = """
Previous Conversation:
User: What services does EBLA provide?
Assistant: EBLA provides infrastructure services including...
"""

# 3. Retrieved Context (RAG Documents)
rag_context = """
Relevant Information:
Source 1: EBLA supports Microsoft-based Infrastructure...
Source 2: Cloud Services include AWS, Azure, Google Cloud...
"""

# 4. User Query (Current Question)
user_query = "Tell me more about their cloud services"

# Final Prompt = System + History + Context + Query
```

### Prompt Engineering Techniques Applied

#### 1. **Instruction Prompting**
Clear, explicit instructions guide the model's behavior:
```
"Provide accurate information based on the context provided."
"Always cite sources when available."
"Be professional and concise."
```

#### 2. **Role Prompting**
Defines the assistant's persona and expertise:
```
"You are an intelligent assistant for EBLA Computer Consultancy."
```

#### 3. **Few-Shot Prompting** (Implicit)
The chat history serves as examples of desired response format and style.

#### 4. **Context Grounding**
Retrieved documents prevent hallucinations:
```
"Answer based on the following context: [RAG results]"
```

---

## 🛠️ Tech Stack

| Component | Technology | Version |
|-----------|-----------|---------|
| **API Framework** | FastAPI | Latest |
| **Database** | SQL Server | Latest |
| **ORM** | SQLAlchemy | 2.0+ |
| **Vector Store** | ChromaDB | 0.5.23 |
| **Embeddings** | Sentence Transformers | all-MiniLM-L6-v2 |
| **LLM Runtime** | Ollama | Latest |
| **LLM Model** | Qwen2.5 | 7B |
| **Validation** | Pydantic | 2.5+ |
| **Environment** | python-dotenv | Latest |

---

## 📦 Installation & Setup

### Prerequisites

1. **Python 3.10+**
2. **Ollama** (for local LLM)
3. **SQL Server** (or SQLite for testing)

### Step 1: Install Ollama & Pull Model

```bash
# Install Ollama (macOS)
brew install ollama

# Or Linux
curl -fsSL https://ollama.com/install.sh | sh

# Start Ollama service
ollama serve

# Pull the Qwen2.5 model
ollama pull qwen2.5:7b
```

### Step 2: Create Virtual Environment

```bash
cd milestones/milestone5
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

Create a `.env` file:

```bash
# Database Configuration (SQL Server)
DATABASE_URL=mssql+pyodbc://username:password@server/database?driver=ODBC+Driver+17+for+SQL+Server

# Or SQLite for testing
# DATABASE_URL=sqlite:///./chat_history.db

# LLM Configuration
LLM_MODEL_NAME=qwen2.5:7b
LLM_BASE_URL=http://localhost:11434
LLM_TEMPERATURE=0.7

# Vector Store Configuration
VECTOR_STORE_PERSIST_DIR=./chroma_db
EMBEDDING_MODEL_NAME=sentence-transformers/all-MiniLM-L6-v2

# RAG Configuration
CHAT_HISTORY_LIMIT=5
DEFAULT_TOP_K=3
DEFAULT_COLLECTION_NAME=documents

# Summarization Configuration
SUMMARY_MAX_MESSAGES=50
```

### Step 5: Initialize Database

The database will be created automatically on first run. To manually initialize:

```bash
python3 -c "from repositories.database.db_connection import init_db; init_db()"
```

**Expected Output:**
```
✅ Database initialized successfully.
✅ Tables created: users, sessions, messages, summaries
```

---

## 🚀 Usage

### Start the API Server

```bash
# Activate virtual environment
source venv/bin/activate

# Start FastAPI server
uvicorn app:app --reload --host 0.0.0.0 --port 8002
```

**Access Points:**
- **Swagger UI**: http://localhost:8002/docs
- **ReDoc**: http://localhost:8002/redoc
- **Health Check**: http://localhost:8002/health

### Start the Streamlit Chat UI

```bash
# Activate virtual environment
source venv/bin/activate

# Run Streamlit app
streamlit run streamlit_app.py
```

**Access Points:**
- **Chat UI**: http://localhost:8501

The UI shows:
- Left column: chat history with user/assistant messages
- Right column: retrieved documents for the latest answer
- Session ID shown under each assistant reply

---

## �📡 API Examples

### 1. Start a New Conversation

```bash
curl -X POST "http://localhost:8002/api/v1/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What services does EBLA provide?",
    "user_id": "user-123",
    "collection_name": "documents",
    "top_k": 3
  }'
```

**Response:**
```json
{
  "status": "success",
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "query": "What services does EBLA provide?",
  "answer": "EBLA provides infrastructure services including Microsoft-based solutions, cloud platforms, and enterprise IT consulting.",
  "sources": [
    {
      "content": "EBLA supports infrastructure services...",
      "metadata": {
        "source": "data/ebla_services.txt"
      },
      "score": 0.45
    }
  ],
  "validation": {
    "used_context": true,
    "used_history": true,
    "context_sources": 3,
    "history_preview": [
      "User: What services does EBLA provide?",
      "Assistant: EBLA provides..."
    ],
    "prompt_preview": "You are an intelligent assistant for EBLA Computer Consultancy..."
  },
  "created_at": "2025-11-28T09:00:00"
}

```

### 2. Continue the Conversation (Context-Aware)

```bash
curl -X POST "http://localhost:8002/api/v1/chat" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Tell me more about their cloud services",
    "user_id": "user-123",
    "session_id": "550e8400-e29b-41d4-a716-446655440000",
    "top_k": 3
  }'
```

**Note**: The AI understands "their" refers to EBLA from the previous message.

### 3. Retrieve Chat History

```bash
curl -X GET "http://localhost:8002/api/v1/history/550e8400-e29b-41d4-a716-446655440000"
```

**Response:**
```json
{
  "session_id": "550e8400-e29b-41d4-a716-446655440000",
  "user_id": "user-123",
  "created_at": "2025-11-28T09:00:00",
  "messages": [
    {
      "message_id": "msg-1",
      "role": "user",
      "content": "What services does EBLA provide?",
      "created_at": "2025-11-28T09:00:00"
    },
    {
      "message_id": "msg-2",
      "role": "assistant",
      "content": "EBLA Computer Consultancy provides...",
      "created_at": "2025-11-28T09:00:05"
    },
    {
      "message_id": "msg-3",
      "role": "user",
      "content": "Tell me more about their cloud services",
      "created_at": "2025-11-28T09:01:00"
    }
  ]
}
```

---

## 🧪 Testing

### Run Unit Tests

```bash
# Test session repository
python3 test/test_session_repo.py

# Test message repository
python3 test/test_message_repo.py

# Test summarization service
python3 test/test_summary_service.py

# Test LLM service
python3 test/test_llm_service.py

# Test vector store
python3 test/test_vector_store.py
```

### Test Coverage

- ✅ **Session Repository**: Create, retrieve, verify sessions
- ✅ **Message Repository**: Add messages, retrieve history, convert to schemas
- ✅ **Summary Repository**: Save and retrieve summaries
- ✅ **LLM Service**: Generate responses, handle errors
- ✅ **Vector Store**: Document indexing, similarity search
- ✅ **Integration**: End-to-end summarization workflow

---

## 🐛 Troubleshooting

### Issue: `ModuleNotFoundError: No module named 'sqlalchemy'`
**Solution**: Activate venv and install dependencies:
```bash
source venv/bin/activate
pip install -r requirements.txt
```

### Issue: `Connection refused` when calling Ollama
**Solution**: Make sure Ollama is running:
```bash
ollama serve
```

### Issue: Database connection error
**Solution**: Verify your `.env` file has the correct `DATABASE_URL`:
```bash
# For SQL Server
DATABASE_URL=mssql+pyodbc://user:pass@server/db?driver=ODBC+Driver+17+for+SQL+Server

# For SQLite (testing)
DATABASE_URL=sqlite:///./chat_history.db
```

### Issue: Port 8002 already in use
**Solution**: Kill the process or use a different port:
```bash
lsof -i :8002
kill -9 <PID>
# Or use different port:
uvicorn app:app --reload --port 8003
```

### Issue: ChromaDB persistence error
**Solution**: Delete and recreate the vector store:
```bash
rm -rf chroma_db/
# Restart the application to rebuild
```

---

## 📊 Comparison with Previous Milestones

| Feature | Milestone 4 | Milestone 5 |
|---------|-------------|-------------|
| **Chat History** | ❌ None | ✅ SQL Database with 4 tables |
| **Context Awareness** | ❌ Single-turn | ✅ Multi-turn conversations |
| **Session Management** | ❌ None | ✅ Session IDs with user tracking |
| **Prompt Engineering** | Basic | ✅ Advanced (System + History + Context) |
| **Summarization** | ❌ None | ✅ Automatic long conversation summarization |
| **Endpoints** | `/chat` | ✅ `/chat`, `/history/{id}` |
| **Database** | ❌ None | ✅ SQL Server with SQLAlchemy ORM |
| **Architecture** | Basic | ✅ Clean Architecture (4 layers) |
| **Testing** | ❌ None | ✅ Comprehensive test suite |

---

## ✅ Milestone Requirements Checklist

### 1. Chat History & ERD ✅
- [x] ER Diagram designed and documented
- [x] Custom table structure (Users, Sessions, Messages, Summaries)
- [x] Database implementation with SQLAlchemy
- [x] Persistence for queries, responses, and context

### 2. Prompt Engineering ✅
- [x] Instruction Prompting implemented
- [x] Role Prompting (EBLA assistant persona)
- [x] Few-shot examples via chat history
- [x] Experimented with prompt improvements

### 3. Integration with RAG Bot ✅
- [x] POST /api/v1/chat endpoint (context-aware)
- [x] GET /api/v1/history/{session_id} endpoint
- [x] Context-aware responses using history + RAG
- [x] Session management and tracking

### 4. Bonus: Summarization ✅
- [x] Automatic summarization of old chat history
- [x] Summary storage in database
- [x] Context optimization for long conversations

### 5. Documentation ✅
- [x] ER Diagram included
- [x] Prompt engineering techniques documented
- [x] Demo examples provided
- [x] Clear setup and usage instructions

---

## 🎯 Learning Objectives Achieved

- ✅ **Understand the importance of chat history** in conversational AI
- ✅ **Learn SQL database design** for chat applications
- ✅ **Master prompt engineering** with multiple context sources
- ✅ **Build context-aware RAG systems** with memory
- ✅ **Apply Clean Architecture** to complex AI systems
- ✅ **Implement conversation summarization** for context management

---

**Status:** ✅ **Completed**  
**Last Updated:** November 28, 2025  
**Author:** Ahmed Balta  
**Project:** EBLA AI Trainee Program - Milestone 6 (Milestone 5 + Streamlit UI)
