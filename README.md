# EBLA AI Trainee Program

This repository is dedicated to the implementation and deliverables of the **EBLA AI Trainee Program**.

---

## 📋 Program Guidelines

### Development Best Practices
• **Dedicate focused time daily** to learning and coding.
• **Keep detailed notes and comments** in your code to track your thought process.
• **Try different approaches.** Treat mistakes as learning opportunities.

### Architecture & Design Patterns
• **MVC (Model-View-Controller):** Follow MVC architecture principles when structuring your code.
  - **Model:** Handle data and business logic
  - **View:** Manage presentation layer (UI/API responses)
  - **Controller:** Process user input and coordinate between Model and View

### Version Control
• **Git/GitHub:** Save and push your code/scripts for each milestone using Git/GitHub.
• **Clear commits:** Each milestone should have clear commits and documentation.
• **Commit messages:** Write descriptive commit messages explaining what was changed and why.

---

## 🎯 Program Milestones

### Milestone 1: Learning Python 
**Status:** 🔄 In Progress  
**Goal:** Gain a solid understanding of Python basics. Write clean, well-structured Python code.

**Objectives:**
• Study Python fundamentals: variables, data types, control flow, functions, modules.
• Practice beginner exercises (loops, conditionals, list/dict operations).
• Apply Google Python Style Guide (type hints, docstrings, naming conventions).

**Deliverables:**
- [ ] A short discussion summary of Python basics.
- [ ] A set of Python scripts showing basic functionalities (loops, functions, classes).

---

### Milestone 2: Understanding RAG & Core Technologies
**Status:** ⏳ Not Started  
**Goal:** Understand Retrieval-Augmented Generation (RAG) architecture. Familiarize with a local LLM (e.g., DeepSeek, GPT-OSS, LLaMA) and an indexing library (LlamaIndex or LangChain).

**Objectives:**
• Studying RAG architecture (retriever, generator, integration).
• Install and configure a local LLM.
• Write initial scripts to interact with the chosen LLM and index a few documents.

**Deliverables:**
- [ ] A discussion summary of RAG concepts.
- [ ] A Python script demonstrating interaction with your chosen local LLM + a simple index build.

---

### Milestone 3: Data Preparation & Indexing
**Status:** ⏳ Not Started  
**Goal:** Preprocess text data, create embeddings, and index documents. Expose these operations via FastAPI endpoints.

**Objectives:**
• Prepare dataset (text files, articles, or documents).
• Generate embeddings using a vector store (FAISS, ChromaDB, Weaviate, etc.).
• Build a FastAPI service with endpoints:
  o POST /index → preprocess and index documents.
  o POST /search → accept a query, return relevant documents.

**Deliverables:**
- [ ] A FastAPI project exposing endpoints to index and manage documents.
- [ ] Documentation explaining how to call the endpoints and what they return.

---

### Milestone 4: Retrieval & LLM Integration
**Status:** ⏳ Not Started  
**Goal:** Implement retrieval of relevant documents. Integrate retrieval results with the local LLM to generate responses. Expose functionality via FastAPI.

**Objectives:**
• Add a retrieval pipeline that fetches documents based on a query.
• Pass retrieved documents to LLM for response generation.
• Extend FastAPI with:
  o POST /ask → accept a query, retrieve documents, and generate an LLM response.

**Deliverables:**
- [ ] A FastAPI project with working endpoints for document retrieval and LLM integration.
- [ ] Example cURL or Postman requests demonstrating usage.

---

### Milestone 5: Chat History, Prompt Engineering & Contextual RAG 
**Status:** ⏳ Not Started  
**Goal:** Understand the importance of chat history and context in conversational AI. Learn the basics of prompt engineering (instruction design, role prompting, few-shot examples). Design and integrate a chat history storage system. Enhance the existing RAG bot with context-aware conversations.

**Objectives:**
1. Chat History & ERD
   o Design an ER Diagram for chat history.
   o Define your own table names and structure to store sessions, messages, and context.
   o Implement persistence (e.g., SQL DB) for storing user queries, bot responses, and retrieved context.
2. Prompt Engineering
   o Learn and apply key prompt engineering concepts:
     • Instruction Prompting: guide the model with clear instructions.
     • Role Prompting: set the assistant's persona.
     • Few-shot Prompting: show examples to improve consistency.
   o Experiment with rewriting prompts to improve response quality.
3. Integration with RAG Bot
   o Extend FastAPI endpoints:
     • POST /chat → accepts a new user message, stores it, retrieves context from history + RAG, then calls the LLM.
     • GET /history/{session_id} → returns the conversation history for a session.
   o Ensure the bot responds with context-aware answers, using both history and retrieved documents.

**Deliverables:**
- [ ] ER Diagram of the chat history database (with custom naming & design).
- [ ] Database implementation for storing chat history.
- [ ] Extended FastAPI endpoints:
  - [ ] POST/chat (context-aware chat with RAG + history).
  - [ ] GET/history/{session_id} (retrieve stored history).
- [ ] A short demo or documentation showing:
  - [ ] How prompts were engineered and improved.
  - [ ] How history + RAG improves the conversation quality.
- [ ] GitHub Repository containing milestone code, with clear commits, branches, and documentation.
- [ ] Add summarization of old chat history (to keep the context short but relevant).[Bonus]

---

### Milestone 6: System Optimization & Final Demo
**Status:** ⏳ Not Started  
**Goal:** Optimize the system for performance, accuracy, and usability. Prepare the system for a final presentation/demo.

**Objectives:**
• Improve embedding/search performance.
• Conduct final testing with multiple datasets.
• Prepare a short presentation/demo script showing how the system works end-to-end.

**Deliverables:**
- [ ] A fully functional RAG system running with FastAPI endpoints.
- [ ] A demo presentation explaining:
  - [ ] System architecture
  - [ ] Challenges and solutions
  - [ ] Example use cases
- [ ] Create a UI chat page showing user messages, bot responses, user sessions and retrieved documents side by side.[Bonus]

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
**Note:** This README will be updated constantly as progress is made through each milestone.

**Last Updated:** November 17, 2025

