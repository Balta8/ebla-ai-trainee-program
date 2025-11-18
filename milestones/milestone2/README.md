### **Milestone 2: Understanding RAG & Core Technologies**
**Goal:** Understand Retrieval-Augmented Generation (RAG) architecture and build a working RAG system with local LLM.

#### Objectives:
- Study RAG architecture (retriever, generator, integration).
- Install and configure a local LLM (Ollama with Qwen2.5:7b).
- Write scripts to interact with the chosen LLM and index documents.
- Apply Google Python Style Guide (type hints, docstrings, naming conventions).

#### Deliverables:
- [x] Discussion summary of RAG concepts
- [x] LocalLLM class for Ollama integration
  - `models/llm_model.py` - LLM wrapper for text generation
- [x] DocumentRetriever class for indexing and retrieval
  - `models/retriever.py` - Document indexing with LlamaIndex
- [x] MVC Architecture Implementation
  - `models/` - LLM and Retriever models
  - `views/view.py` - Display/presentation layer
  - `controllers/rag_controller.py` - Coordinates RAG workflow
  - `main.py` - Main entry point for RAG system
- [x] Sample data for testing
  - `data/sample.txt` - Sample document for indexing

---

# 📘 Discussion Summary — RAG Concepts

## **What is RAG (Retrieval-Augmented Generation)?**

RAG is an AI framework that combines **information retrieval** with **text generation** to produce more accurate and contextually relevant responses.

### **Key Components:**

#### **1. Retriever**
- Searches through a knowledge base (documents, databases)
- Uses embeddings and vector similarity to find relevant information
- Returns top-k most relevant documents based on query

#### **2. Generator (LLM)**
- Takes retrieved documents as context
- Generates responses based on the retrieved information
- Produces more accurate answers grounded in actual data

#### **3. Integration**
- Query → Retriever finds relevant docs → LLM generates answer using docs
- Reduces hallucinations by grounding responses in real data
- Allows LLMs to access up-to-date or domain-specific information

---

## **Why Use RAG?**

✅ **Reduces hallucinations** - Answers based on actual documents  
✅ **Up-to-date information** - Can index recent documents  
✅ **Domain-specific knowledge** - Add your own data  
✅ **Cost-effective** - No need to retrain LLMs  
✅ **Transparent** - Can cite sources used

---

## **Technologies Used in This Implementation**

### **LLM: Ollama + Qwen2.5:7b**
- **Ollama:** Tool for running LLMs locally
- **Qwen2.5:7b:** 7-billion parameter model by Alibaba
- Runs completely offline, no API costs

### **Indexing: LlamaIndex**
- Framework for connecting LLMs with external data
- Handles document loading, chunking, and indexing
- Provides query engines for retrieval

### **Embeddings: HuggingFace (BAAI/bge-small-en-v1.5)**
- Converts text to vector representations
- Free and runs locally
- Efficient for similarity search

### **Vector Storage**
- In-memory vector store (no external database needed)
- Fast for small-to-medium datasets
- Can be upgraded to FAISS, Chroma, or Weaviate later

---

## 📂 Project Structure

```
milestone2/
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
├── main.py                            # Main entry point
├── models/
│   ├── llm_model.py                   # LocalLLM wrapper for Ollama
│   └── retriever.py                   # DocumentRetriever with LlamaIndex
├── views/
│   └── view.py                        # Display layer
├── controllers/
│   └── rag_controller.py              # RAG workflow coordinator
└── data/
    └── sample.txt                     # Sample document
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- Ollama installed ([ollama.ai](https://ollama.ai))
- Git

### Installation

1. **Install Ollama and pull the model**
   ```bash
   # Install Ollama from https://ollama.ai
   
   # Pull the Qwen model
   ollama pull qwen2.5:7b
   
   # Verify Ollama is running
   ollama list
   ```

2. **Navigate to milestone2 folder**
   ```bash
   cd milestone2
   ```

3. **Create virtual environment** (Optional but recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   ```

4. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🎮 Running the Project

### **Run the Full RAG System:**
```bash
python3 main.py
```

This will:
1. Load documents from `data/sample.txt`
2. Build vector index
3. Start interactive Q&A session
4. Type 'quit' to exit

### **Test Individual Components:**

**Test LLM only:**
```bash
python3 models/llm_model.py
```

**Test Retriever only:**
```bash
python3 models/retriever.py
```

---

## 💡 Example Usage

```
Building document index...
Indexed 1 documents.

Enter your question (or 'quit' to exit): What is Python?

Retrieving relevant documents...
Generating response...
Answer: Python is a high-level, interpreted programming language 
known for its simplicity and readability...
```

---

## 📚 Key Learnings

### **RAG Architecture**
- ✅ Understanding retriever-generator pipeline
- ✅ Embedding-based similarity search
- ✅ Context-aware response generation

### **Local LLM Integration**
- ✅ Running Ollama locally
- ✅ Connecting Python to LLM
- ✅ Error handling and timeouts

### **Document Indexing**
- ✅ Converting text to embeddings
- ✅ Vector storage and retrieval
- ✅ Query processing

### **MVC Architecture**
- ✅ Separating concerns (Model, View, Controller)
- ✅ Modular and testable code
- ✅ Clean code principles

