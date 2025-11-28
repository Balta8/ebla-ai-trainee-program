# EBLA AI Trainee Program

This repository is dedicated to the implementation and deliverables of the **EBLA AI Trainee Program**.

---

## 📋 Program Guidelines

### Development Best Practices
- **Dedicate focused time daily** to learning and coding.
- **Keep detailed notes and comments** in your code to track your thought process.
- **Try different approaches.** Treat mistakes as learning opportunities.

### Architecture & Design Patterns
• **MVC (Model-View-Controller):** Follow MVC architecture principles when structuring your code.
  - **Model:** Handle data and business logic
  - **View:** Manage presentation layer (UI/API responses)
  - **Controller:** Process user input and coordinate between Model and View

### Version Control
- **Git/GitHub:** Save and push your code/scripts for each milestone using Git/GitHub.
- **Clear commits:** Each milestone should have clear commits and documentation.
- **Commit messages:** Write descriptive commit messages explaining what was changed and why.

---

## 🎯 Program Milestones

### Milestone 1: Learning Python ✅
**Status:** Completed  
**Branch:** `main`  
**Folder:** [`milestones/milestone1/`](./milestones/milestone1/)

**Goal:** Gain a solid understanding of Python basics and write clean, structured code.

**Key Deliverables:**
- ✅ Python fundamentals exercises (loops, conditionals, functions)
- ✅ MVC architecture implementation
- ✅ Google Python Style Guide compliance

[View Milestone 1 Details →](./milestones/milestone1/README.md)

---

### Milestone 2: Understanding RAG & Core Technologies ✅
**Status:** Completed  
**Branch:** `main`  
**Folder:** [`milestones/milestone2/`](./milestones/milestone2/)

**Goal:** Understand Retrieval-Augmented Generation (RAG) architecture and build a working RAG system with local LLM.

**Key Deliverables:**
- ✅ RAG concepts documentation and discussion summary
- ✅ Local LLM integration (Ollama + Qwen2.5:7b)
- ✅ Document indexing with LlamaIndex
- ✅ MVC architecture implementation
- ✅ Interactive Q&A system with vector search
- ✅ Google Python Style Guide compliance

[View Milestone 2 Details →](./milestones/milestone2/README.md)

---

### Milestone 3: Data Preparation & Indexing ✅
**Status:** Completed  
**Branch:** `main`  
**Folder:** [`milestones/milestone3/`](./milestones/milestone3/)

**Goal:** Preprocess text data, create embeddings, and index documents via FastAPI endpoints.

**Key Deliverables:**
- ✅ FastAPI REST API with `/index` and `/search` endpoints
- ✅ Document indexing (PDF & TXT) with LangChain
- ✅ ChromaDB vector store integration
- ✅ Pydantic schemas for request/response validation
- ✅ MVC architecture with Dependency Injection
- ✅ Advanced logging system
- ✅ Comprehensive API documentation (Swagger UI)

[View Milestone 3 Details →](./milestones/milestone3/README.md)

---

### Milestone 4: Retrieval & LLM Integration ✅
**Status:** Completed  
**Branch:** `main`  
**Folder:** [`milestones/milestone4/`](./milestones/milestone4/)

**Goal:** Implement retrieval of relevant documents and integrate with local LLM.

**Key Deliverables:**
- ✅ LLM Integration (Ollama + Qwen2.5:7b)
- ✅ RAG Pipeline (Retrieval + Generation)
- ✅ Chat Endpoint (`POST /api/v1/chat`)
- ✅ Context-aware responses with source attribution
- ✅ Clean Architecture (Router -> Controller -> Service -> Utils)
- ✅ Prompt Engineering

[View Milestone 4 Details →](./milestones/milestone4/README.md)

---

### Milestone 5: Chat History, Prompt Engineering & Contextual RAG ✅
**Status:** Completed  
**Branch:** `milestone5`  
**Folder:** [`milestones/milestone5/`](./milestones/milestone5/)

**Goal:** Implement chat history storage and prompt engineering techniques.

**Key Deliverables:**
- ✅ SQL Server database with 4 tables (Users, Sessions, Messages, Summaries)
- ✅ FastAPI endpoints: `/api/v1/chat`, `/api/v1/history/{session_id}`
- ✅ Context-aware RAG with chat history
- ✅ Advanced prompt engineering (System + History + Context + Query)
- ✅ Automatic conversation summarization
- ✅ Clean Architecture (4 layers)
- ✅ Comprehensive test suite

[View Milestone 5 Details →](./milestones/milestone5/README.md)

---

### Milestone 6: Streamlit UI for Chat RAG ✅
**Status:** Completed  
**Branch:** `milestone6`  
**Folder:** [`milestones/milestone6/`](./milestones/milestone6/)

**Goal:** Add a user-friendly chat interface for the RAG system.

**Key Deliverables:**
- ✅ Streamlit chat UI with side-by-side layout
- ✅ Real-time chat with session persistence
- ✅ Display of retrieved documents alongside responses
- ✅ Session ID tracking

[View Milestone 6 Details →](./milestones/milestone6/README.md)

---

## 🛠️ Tech Stack

- **Language:** Python 3.13+
- **Framework:** FastAPI (Milestone 3+)
- **UI:** Streamlit (Milestone 6)
- **LLM:** Ollama (Qwen2.5:7b) - Local, offline
- **Indexing:** LlamaIndex, LangChain
- **Embeddings:** HuggingFace (BAAI/bge-large-en-v1.5, sentence-transformers/all-MiniLM-L6-v2)
- **Vector Store:** In-memory, ChromaDB (persistent storage)
- **Database:** SQL Server (Milestone 5+)

---

## 📂 Repository Structure

```
ebla-ai-trainee-program/
├── README.md                          # Project overview (this file)
├── requirements.txt                   # Python dependencies
├── .gitignore                        # Git ignore rules
└── milestones/
    ├── milestone1/                   # ✅ Milestone 1: Python Fundamentals
    │   ├── README.md                 # Milestone 1 documentation
    │   ├── main.py                   # MVC demo
    │   ├── Controller/               # MVC Controller
    │   ├── Model/                    # MVC Model
    │   ├── View/                     # MVC View
    │   └── exercises/                # Python exercises
    ├── milestone2/                   # ✅ Milestone 2: RAG System
    │   ├── README.md                 # Milestone 2 documentation
    │   ├── main.py                   # RAG system entry point
    │   ├── controllers/              # RAG Controller
    │   ├── services/                 # Business Logic (RAG, Vector Store)
    │   ├── views/                    # Display layer
    │   ├── data/                     # Sample documents
    │   └── requirements.txt          # Milestone 2 dependencies
    ├── milestone3/                   # ✅ Milestone 3: FastAPI RAG
    │   ├── README.md                 # Milestone 3 documentation
    │   ├── app.py                    # FastAPI application
    │   ├── main.py                   # CLI tool
    │   ├── controllers/              # Document controller
    │   ├── services/                 # Document & Vector Store services
    │   ├── models/                   # Pydantic schemas (API models)
    │   ├── routers/                  # API endpoints
    │   ├── views/                    # CLI & Base views
    │   ├── utils/                    # Logging & Helpers
    │   ├── data/                     # EBLA documents
    │   └── requirements.txt          # Milestone 3 dependencies
    ├── milestone4/                   # ✅ Milestone 4: Retrieval & LLM
    │   ├── README.md                 # Milestone 4 documentation
    │   ├── app.py                    # FastAPI app
    │   ├── routers/                  # Chat endpoints
    │   ├── controllers/              # RAG orchestration
    │   ├── services/                 # Business logic
    │   ├── models/                   # Data models & Schemas
    │   ├── utils/                    # Helper functions
    │   ├── views/                    # Presentation layer
    │   └── requirements.txt          # Dependencies
    ├── milestone5/                   # ✅ Milestone 5: Chat History & Context
    │   ├── README.md                 # Milestone 5 documentation
    │   ├── app.py                    # FastAPI application
    │   ├── config.py                 # Settings
    │   ├── requirements.txt          # Dependencies
    │   ├── .env                      # Environment variables
    │   ├── repositories/             # Data Access Layer
    │   ├── models/                   # SQLAlchemy ORM
    │   ├── schemas/                  # Pydantic schemas
    │   ├── services/                 # Business Logic
    │   ├── routers/                  # API endpoints
    │   ├── utils/                    # Helpers
    │   ├── test/                     # Test suite
    │   ├── data/                     # Source documents
    │   └── docs/                     # Documentation
    └── milestone6/                   # ✅ Milestone 6: Streamlit UI
        ├── README.md                 # Milestone 6 documentation
        ├── streamlit_app.py          # Streamlit chat UI
        ├── requirements.txt          # Dependencies
        └── docs/                     # Screenshots
```

---

## 🚀 Quick Start

### Clone the Repository
```bash
git clone https://github.com/Balta8/ebla-ai-trainee-program.git
cd ebla-ai-trainee-program
```

### Explore Milestones
Each milestone has its own folder with detailed documentation:
```bash
cd milestones/milestone1
cat README.md
```

### Run Examples
```bash
# Navigate to a milestone
cd milestones/milestone1

# Run the code
python3 main.py
```

---

## 📊 Progress Tracking

| Milestone | Status | Branch | Folder |
|-----------|--------|--------|--------|
| 1. Python Fundamentals | ✅ Complete | `main` | `milestones/milestone1/` |
| 2. RAG & Core Tech | ✅ Complete | `main` | `milestones/milestone2/` |
| 3. Data & Indexing | ✅ Complete | `main` | `milestones/milestone3/` |
| 4. Retrieval & LLM | ✅ Complete | `main` | `milestones/milestone4/` |
| 5. Chat & Prompts | ✅ Complete | `milestone5` | `milestones/milestone5/` |
| 6. Streamlit UI | ✅ Complete | `milestone6` | `milestones/milestone6/` |

---

**Last Updated:** November 28, 2025

**Note:** This README is updated constantly as progress is made through each milestone.

