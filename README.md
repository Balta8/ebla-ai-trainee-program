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

### Milestone 1: Learning Python ✅
**Status:** Completed  
**Branch:** `milestone1`  
**Folder:** [`milestones/milestone1/`](./milestones/milestone1/)

**Goal:** Gain a solid understanding of Python basics and write clean, structured code.

**Key Deliverables:**
- ✅ Python fundamentals exercises (loops, conditionals, functions)
- ✅ MVC architecture implementation
- ✅ Google Python Style Guide compliance

[View Milestone 1 Details →](./milestones/milestone1/README.md)

---

### Milestone 2: Understanding RAG & Core Technologies
**Status:** ⏳ Not Started  
**Branch:** `milestone2` (to be created)  
**Folder:** `milestones/milestone2/` (to be created)

**Goal:** Understand Retrieval-Augmented Generation (RAG) architecture. Familiarize with a local LLM and indexing library.

**Objectives:**
• Study RAG architecture (retriever, generator, integration)
• Install and configure a local LLM
• Write initial scripts to interact with the chosen LLM and index documents

---

### Milestone 3: Data Preparation & Indexing
**Status:** ⏳ Not Started  
**Goal:** Preprocess text data, create embeddings, and index documents via FastAPI endpoints.

---

### Milestone 4: Retrieval & LLM Integration
**Status:** ⏳ Not Started  
**Goal:** Implement retrieval of relevant documents and integrate with local LLM.

---

### Milestone 5: Chat History, Prompt Engineering & Contextual RAG
**Status:** ⏳ Not Started  
**Goal:** Implement chat history storage and prompt engineering techniques.

---

### Milestone 6: System Optimization & Final Demo
**Status:** ⏳ Not Started  
**Goal:** Optimize the system for performance and prepare final presentation.

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Framework:** FastAPI
- **LLM:** Qwen2.5:7b
- **Indexing:** LangChain
- **Vector Store:** TBD (FAISS / ChromaDB / Weaviate)
- **Database:** TBD (SQLite / PostgreSQL)

---

## 📂 Repository Structure

```
ebla-ai-trainee-program/
├── README.md                          # Project overview (this file)
├── requirements.txt                   # Python dependencies
├── .gitignore                        # Git ignore rules
└── milestones/
    ├── milestone1/                   # Milestone 1: Python Fundamentals
    │   ├── README.md                 # Milestone 1 documentation
    │   ├── main.py                   # MVC demo
    │   ├── Controller/               # MVC Controller
    │   ├── Model/                    # MVC Model
    │   ├── View/                     # MVC View
    │   └── exercises/                # Python exercises
    ├── milestone2/                   # Milestone 2 (coming soon)
    ├── milestone3/                   # Milestone 3 (coming soon)
    └── ...
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
| 1. Python Fundamentals | ✅ Complete | `milestone1` | `milestones/milestone1/` |
| 2. RAG & Core Tech | ⏳ Not Started | - | - |
| 3. Data & Indexing | ⏳ Not Started | - | - |
| 4. Retrieval & LLM | ⏳ Not Started | - | - |
| 5. Chat & Prompts | ⏳ Not Started | - | - |
| 6. Final Demo | ⏳ Not Started | - | - |

---

**Last Updated:** November 17, 2025

**Note:** This README will be updated constantly as progress is made through each milestone.

