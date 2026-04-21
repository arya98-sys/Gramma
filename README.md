# Gramma AI: Neural Writing Architecture 🌑✨

[![Python](https://img.shields.io/badge/Backend-Python%203.9%2B-blue?logo=python)](https://www.python.org/)
[![React](https://img.shields.io/badge/Frontend-React%2018-61DAFB?logo=react)](https://reactjs.org/)
[![Model](https://img.shields.io/badge/AI%20Model-T5--Transformer-green?logo=huggingface)](https://huggingface.co/models)


# Gramma AI: 

A professional, dark-themed grammar correction suite powered by **T5-Base Transformers** and a **FastAPI** backend. This project features a high-end "Dark Silk" interface built with **React** and **Tailwind CSS v3**.

---

## 👥 The Team
* **Hemendra Saraswat** – DevOps & Project Lead
* **Arya Mishra & Abhinav Pal** – Backend & AI Integration
* **Ayush Rastogi & Deepanshu Lamba** – Frontend & UI/UX Design

---

## 🚀 Deployment Instructions

Follow these steps in order to set up the environment and launch the application.

### 1. Backend Setup (AI Engine)

**Step A: Navigate & Environment**
```bash
cd backend
python -m venv venv
```
**Step B: Activate Virtual Environment**

```bash
# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
```
**Step C: Install Dependencies**

```bash
pip install -r requirements.txt
```
**Step D: Run Server**

```bash
python main.py
```
### 2. Frontend Setup 

**Step A: Navigate & Install**

```bash
cd frontend
npm install
```
**Step B: Launch UI**

```bash
npm start
```
### 🛠️ GitHub Workflow (The Professional Protocol)
To keep the repository synchronized and avoid "rejected" errors, follow this Pull-Add-Commit-Push sequence.

**Step 1: Pull**
Always download the latest changes from the remote repository before starting:

```bash
git pull origin main --rebase
```
**Step 2: Stage Changes**

```bash
git add .
```
**Step 3: Commit**
Save your local work with a clear message:

```bash
git commit -m "feat: updated Dark Silk UI transitions"
```
**Step 4: Push**

```bash
git push -u origin main
```
### 🎨 Design Philosophy: "Dark Silk"
* The interface is designed with a Premium SaaS aesthetic:

* Backdrop: Deep midnight gradients (#1a1c2c to #0d0e14).

* Glassmorphism: Cards use backdrop-filter: blur(16px) for a frosted glass look.

* Typography: High-contrast serif italics for AI suggestions.

### 📦 Technical Stack
* **Frontend: React.js, Tailwind CSS, Axios**

* **Backend: FastAPI (Python), Uvicorn**

* **AI Model: HappyTransformer (T5-Base)**

* **Version Control: Git & GitHub**

© 2026 CS Department Project • Built for Excellence.
