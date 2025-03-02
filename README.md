# RepoReview 🤖📊

Welcome to **RepoReview**, an AI-powered tool designed to analyze GitHub repositories and generate insightful reviews for company recruiters. This project helps recruiters **understand a developer's coding skills** by evaluating repositories based on various software quality parameters.

## 📌 Project Overview

RepoReview is an AI agent that goes through a **GitHub repository** and assesses it based on:
- ✅ **Tests** – Presence and quality of unit/integration tests.
- 🏗️ **Code Quality** – Clean, maintainable, and efficient code.
- ⚡ **Optimization** – Performance improvements and best practices.
- 📖 **Readability** – Proper naming, comments, and structure.
- 📚 **Documentation** – Well-maintained README, docstrings, and guides.
- 👥 **Team Workability** – Collaboration metrics, PR reviews, and commit history.

## 🏗️ Workspace Structure

📂 **.github/** - GitHub workflow and automation files.  
📂 **docs/** - Documentation and project references.  
📂 **src/** - Source code for AI review components.  
📂 **tests/** - Unit tests for ensuring AI functionality. 
📄 **.gitignore** - Files to be ignored by Git.  
📜 **LICENSE** - Project licensing information.  
📘 **README.md** - This documentation file.  
📋 **requirements.txt** - Dependencies required for the project.  
🐍 **test.py** - Initial test script for AI review module.  

## 🛠️ Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/ivanrj7j/RepoReview.git
   ```
2. Navigate to the project directory:
   ```bash
   cd RepoReview
   ```
3. Set up a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run initial tests:
   ```bash
   python test.py
   ```

## 📢 Contribution Guidelines

### 🔧 How to Contribute

1. **Create a new branch** for your feature/fix:
   ```bash
   git checkout -b feature-branch-name
   ```
2. **Make your changes** and ensure they follow best practices.
3. **Stage and commit your changes:**
   ```bash
   git add .
   git commit -m "Describe your changes"
   ```
4. **Push your changes** to the repository:
   ```bash
   git push origin feature-branch-name
   ```
5. **Create a pull request (PR):**
   - Navigate to the repository on GitHub.
   - Click on "Pull Requests" → "New Pull Request".
   - Select your branch and compare it with the main branch.
   - Submit the pull request for review.

### ✅ Best Practices

- Follow **PEP 8** coding guidelines.
- Write **clear and concise commit messages**.
- Keep PRs **small and focused**.
- **Document your code** for better maintainability.
- **Test your changes** before pushing.

## 🚀 To-Do List

- 🔗 **GitHub Interface** – Fetch repositories, extract metadata, and analyze commit history. ✅
- 🧠 **AI Review** – Implement NLP and ML models to evaluate repositories. ✅
- 🎨 **Frontend in Gradio** – Create a user-friendly interface for recruiters to view AI-generated reports. ✅

## 🔥 Join the Project!

This project aims to help recruiters make **data-driven hiring decisions** based on **real coding practices**. Whether you're a developer, AI enthusiast, or UX designer, your contributions are welcome! 😃

