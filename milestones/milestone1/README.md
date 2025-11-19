### **Milestone 1: Learning Python**
**Goal:** Gain a solid understanding of Python basics and write clean, structured code.

#### Objectives:
- Study Python fundamentals: variables, data types, control flow, functions, modules.
- Practice beginner exercises (loops, conditionals, list/dict operations).
- Apply Google Python Style Guide (type hints, docstrings, naming conventions).

#### Deliverables:
- [x] Short discussion summary of Python basics  
- [x] Python scripts showing basic functionalities (loops, functions, classes)
  - `exercises/conditionals.py` - Control flow examples (if/elif/else)
  - `exercises/Functions.py` - Function definitions with examples
  - `exercises/Loops.py` - Loop implementations (for/while)
- [x] MVC Architecture Implementation
  - `Model/person_model.py` - Person data model
  - `View/person_view.py` - Display/presentation layer
  - `Controller/person_controller.py` - Coordinates Model and View
  - `main.py` - Demo script showing MVC in action

---

# 📘 1. Discussion Summary — Python Basics

# Source : [w3schools](https://www.w3schools.com/python/)

## **1. Variables & Data Types**

Python uses dynamic typing and supports common types:

* `int`, `float`, `str`, `bool`
* `list`, `tuple`, `set`, `dict`

## **2. Control Flow**

Python uses:

* `if / elif / else`
* `for`, `while`
  Indentation defines blocks.

## **3. Functions**

Functions allow reusable logic with:

* Arguments
* Return values

## **4. Clean Code Principles (Google Style Guide)**

* snake_case
* docstrings
* type hints

---

## 📂 Project Structure

```
ebla-ai-trainee-program/
├── README.md                           # Project documentation
├── requirements.txt                    # Python dependencies
├── main.py                            # MVC demo entry point
├── Controller/
│   └── person_controller.py           # Controller layer 
├── Model/
│   └── person_model.py                # Model layer 
├── View/
│   └── person_view.py                 # View layer 
└── exercises/
    ├── conditionals.py                # Control flow exercises
    ├── Functions.py                   # Function examples
    └── Loops.py                       # Loop implementations
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or higher
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Balta8/ebla-ai-trainee-program.git
   cd ebla-ai-trainee-program
   ```

2. **Create virtual environment** (Optional but recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   # or
   venv\Scripts\activate     # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   *Note: Milestone 1 uses only standard Python libraries, so no external packages are needed yet.*

### Running the Project

**Run MVC Demo:**
```bash
python3 main.py
```

**Run Individual Exercises:**
```bash
# Control flow examples
python3 exercises/conditionals.py

# Function demonstrations
python3 exercises/Functions.py

# Loop implementations
python3 exercises/Loops.py
```

