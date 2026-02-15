# Python + DSA Interview Prep Suite

A curated set of Python and data-structures/algorithms (DSA) resources designed for FAANG-style technical interviews.

This repo is meant to be used as a **practice workbook**: you solve the questions in the notebooks, then compare against comprehensive model solutions with detailed explanations and code examples.

---

## 🚀 Open directly in Google Colab

Click these links to launch the notebooks in Google Colab:

- **Python fundamentals questions:**
  - <a href="https://colab.research.google.com/github/nitishkumarnitc/PythonDSAInterviewPrep/blob/main/pythonprep.ipynb" target="_blank" rel="noopener noreferrer">Open `pythonprep.ipynb` in Colab</a>
- **Python fundamentals solutions:**
  - <a href="https://colab.research.google.com/github/nitishkumarnitc/PythonDSAInterviewPrep/blob/main/pythonprep_solutions.ipynb" target="_blank" rel="noopener noreferrer">Open `pythonprep_solutions.ipynb` in Colab</a>
- **Python drills:**
  - <a href="https://colab.research.google.com/github/nitishkumarnitc/PythonDSAInterviewPrep/blob/main/pythonprep_drills.ipynb" target="_blank" rel="noopener noreferrer">Open `pythonprep_drills.ipynb` in Colab</a>
- **DSA questions:**
  - <a href="https://colab.research.google.com/github/nitishkumarnitc/PythonDSAInterviewPrep/blob/main/DSA/dsa_prep.ipynb" target="_blank" rel="noopener noreferrer">Open `DSA/dsa_prep.ipynb` in Colab</a>
- **DSA solutions:**
  - <a href="https://colab.research.google.com/github/nitishkumarnitc/PythonDSAInterviewPrep/blob/main/DSA/dsa_prep_solutions.ipynb" target="_blank" rel="noopener noreferrer">Open `DSA/dsa_prep_solutions.ipynb` in Colab</a>

---

## Contents

### Python fundamentals

- `pythonprep.ipynb`
  - 50 carefully chosen Python fundamentals questions.
  - Covers semantics, data structures, OOP, exceptions, concurrency, iterators/generators, decorators, tooling, and more.
  - Organized in 5 sections: Core Python Semantics, Data Structures & OOP, Advanced Features, Generators & Iterators, Concurrency & Performance.

- `pythonprep_solutions.ipynb`
  - **Complete solutions for all 50 questions** in integrated format:
    - **Question**: Full question text
    - **Answer**: Detailed explanation of the concept
    - **Example Code**: Runnable Python code with comments and test cases
  - All questions include comprehensive explanations and working examples.

- `pythonprep_drills.ipynb`
  - **Flashcards** (Q1–Q10) with one markdown answer cell per question so you can write your own responses.
  - **Coding drills** with `TODO` implementations to practice writing idiomatic Python.

### DSA (Data Structures & Algorithms)

- `DSA/dsa_prep.ipynb`
  - 50 core DSA problems grouped into 6 sections:
    - Arrays & basic algorithms
    - Strings & hashing
    - Two pointers & sliding window
    - Linked lists & stacks
    - Trees & graphs
    - Dynamic programming & greedy
  - Each problem is its own markdown cell so you can insert a code cell right below it.

- `DSA/dsa_prep_solutions.ipynb`
  - **Complete solutions for all 50 problems** in integrated format:
    - **Question**: Full problem statement
    - **Approach**: Detailed explanation of the solution strategy
    - **Complexity**: Time and space complexity analysis
    - **Pseudocode**: Structured pseudocode for the algorithm
    - **Solution**: Complete Python implementation with test cases
  - All problems include comprehensive explanations, pseudocode, and working code.

- `DSA/dsa_reference_solutions.py`
  - Clean, type-annotated Python implementations of the DSA problems.
  - Each function includes a short docstring describing the idea and complexity.

---

## How to use this repo

1. **Set up environment**
   - Install Python 3.9+.
   - Install Jupyter or VS Code with the Python extension, or use Google Colab (links above).
   - (Optional but recommended) create and activate a virtual environment.

2. **Open the notebooks**
   - Open `pythonprep.ipynb` / `DSA/dsa_prep.ipynb` in Jupyter, VS Code, or Colab.

3. **Attempt questions first**
   - For each question/problem:
     - Read the prompt carefully.
     - Insert a **code cell** under the question.
     - Implement your solution and write down **time/space complexity** and **edge cases** in comments.

4. **Then check solutions**
   - Open `pythonprep_solutions.ipynb` / `DSA/dsa_prep_solutions.ipynb`.
   - Read the **detailed explanation** with question, answer/approach, and example code all together.
   - For DSA problems, review the **pseudocode** to understand the algorithm structure.
   - Run the example code cells and compare your approach, complexity, and edge cases.

5. **Drills and reference code**
   - Use `pythonprep_drills.ipynb` for spaced-repetition style review (flashcards) and to get quick hands-on practice via the coding exercises.
   - Use `DSA/dsa_reference_solutions.py` as a reference implementation library and for importing functions during practice sessions.

---

## Suggested folder structure

The key files for this prep suite are:

- `pythonprep.ipynb`
- `pythonprep_solutions.ipynb`
- `pythonprep_drills.ipynb`
- `DSA/dsa_prep.ipynb`
- `DSA/dsa_prep_solutions.ipynb`
- `DSA/dsa_reference_solutions.py`

You can freely add your own notebooks or scripts (e.g., `experiments/`, `notes/`, `tests/`).



## Initial Git setup (local)

If you havent already initialized a git repo here, you can do:

```bash
git init
git add .
git commit -m "Initial commit: Python + DSA interview prep suite"
```

Then create a new repository on GitHub and follow their instructions, typically something like:

```bash
git remote add origin git@github.com:<your-username>/<your-repo-name>.git
git push -u origin main
```

---

## Notes / TODOs

- ✅ All 50 Python questions have complete solutions with integrated question, answer, and example code.
- ✅ All 50 DSA problems have complete solutions with question, approach, complexity, pseudocode, and code.
- Add simple unit tests for the reference DSA functions (optional enhancement).
