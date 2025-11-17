# EBLA AI Trainee Program

This repository is dedicated to the implementation and deliverables of the **EBLA AI Trainee Program**.

---

## 📋 Program Guidelines

### 🔧 Development Best Practices
- **Dedicate focused time daily** to learning and coding.
- **Keep detailed notes and comments** in your code to track your thought process.
- **Try different approaches.** Treat mistakes as learning opportunities.

### 🧱 Architecture & Design Patterns
**MVC (Model-View-Controller):** Follow MVC architecture principles when structuring your code.

- **Model:** Handles data and business logic  
- **View:** Manages the presentation layer (UI/API responses)  
- **Controller:** Processes user input & coordinates between Model and View  

### 🌿 Version Control
- **Git/GitHub:** Save and push your code/scripts for each milestone.
- **Clear commits:** Each milestone should have clear, meaningful commits.
- **Commit messages:** Write descriptive messages explaining what changed and why.

---

## 🎯 Program Milestones

---

### **Milestone 1: Learning Python**
**Status:** 🔄 *In Progress*  
**Goal:** Gain a solid understanding of Python basics and write clean, structured code.

#### Objectives:
- Study Python fundamentals: variables, data types, control flow, functions, modules.
- Practice beginner exercises (loops, conditionals, list/dict operations).
- Apply Google Python Style Guide (type hints, docstrings, naming conventions).

#### Deliverables:
- [ ] Short discussion summary of Python basics  
- [ ] Python scripts showing basic functionalities (loops, functions, classes)

---

### **Milestone 2: Understanding RAG & Core Technologies**
**Status:** ⏳ *Not Started*  
**Goal:** Understand Retrieval-Augmented Generation (RAG) and get familiar with a local LLM + indexing library.

#### Objectives:
- Study RAG architecture (retriever, generator, integration)
- Install & configure a local LLM
- Write initial scripts to interact with the LLM and index sample documents

#### Deliverables:
- [ ] RAG concept summary  
- [ ] Python script for local LLM interaction + basic indexing

---

### **Milestone 3: Data Preparation & Indexing**
**Status:** ⏳ *Not Started*  
**Goal:** Preprocess text, create embeddings, and index documents. Expose functionality via FastAPI.

#### Objectives:
- Prepare dataset (text files, articles, documents)
- Generate embeddings using a vector store (FAISS / ChromaDB / Weaviate)
- Build FastAPI endpoints:
  - `POST /index` → preprocess + index documents  
  - `POST /search` → query → return relevant documents  

#### Deliverables:
- [ ] FastAPI project for indexing/search  
- [ ] Documentation for endpoints usage

---

### **Milestone 4: Retrieval & LLM Integration**
**Status:** ⏳ *Not Started*  
**Goal:** Implement document retrieval and integrate results with LLM. Extend FastAPI endpoints.

#### Objectives:
- Add retrieval pipeline  
- Pass retrieved docs to LLM for response generation  
- Extend FastAPI with:
  - `POST /ask` → query → retrieve → LLM response  

#### Deliverables:
- [ ] Fully working retrieval + LLM integration  
- [ ] Example cURL/Postman usage

---

### **Milestone 5: Chat History, Prompt Engineering & Contextual RAG**
**Status:** ⏳ *Not Started*  
**Goal:** Add chat history storage, improve prompts, and make RAG context-aware.

#### Objectives:
1. **Chat History & ERD**
   - Design ERD  
   - Define tables (sessions, messages, context)  
   - Implement DB persistence  

2. **Prompt Engineering**
   - Instruction, role, and few-shot prompting  
   - Experiment with improving prompts  

3. **Integration**
   - Extend FastAPI:
     - `POST /chat` → history + RAG  
     - `GET /history/{session_id}` → retrieve chat logs  

#### Deliverables:
- [ ] ERD  
- [ ] Database implementation  
- [ ] Extended FastAPI endpoints  
- [ ] Demo showing prompt engineering + context improvements  
- [ ] Summarization of old history *(Bonus)*

---

### **Milestone 6: System Optimization & Final Demo**
**Status:** ⏳ *Not Started*  
**Goal:** Optimize, test, and prepare a full demo.

#### Objectives:
- Improve embedding/search performance  
- Test with multiple datasets  
- Prepare presentation explaining system workflow  

#### Deliverables:
- [ ] Fully functional RAG system  
- [ ] Demo presentation  
- [ ] Optional UI chat page *(Bonus)*

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+  
- **Framework:** FastAPI  
- **LLM:** Qwen2.5:7b  
- **Indexing:** LangChain  
- **Vector Store:** TBD (FAISS / ChromaDB / Weaviate)  
- **Database:** TBD (SQLite / PostgreSQL)

---

## 📂 Project Structure

```
ebla-ai-trainee-program/
├── README.md

```

---

**Last Updated:** November 17, 2025

**Note:** This README will be updated constantly as progress is made through each milestone.

