# StudyPilot AI 🚀
### *Your AI-Powered Academic Copilot*

> **PromptWars X HackArena Entry**  
> **Category**: AI, Prompt Engineering, Data Science, Practical Productivity Solutions

---

## 🌟 Overview

**StudyPilot AI** is a complete, hackathon-ready academic assistant built to solve college student learning friction. Instead of being a simple generic chat interface, StudyPilot AI delivers structured, actionable tools:
1. **📊 Academic Dashboard**: Live metrics, study hour charts, subject mastery breakdown, and AI smart recommendations.
2. **📅 AI Study Planner**: Form-driven schedule builder with topic prioritization, daily pomodoro blocks, and exam prep strategies.
3. **👨‍🏫 AI Concept Tutor**: Multi-level tutoring (Beginner, Intermediate, Advanced) with step-by-step logic, runnable code snippets, common pitfalls, and interactive practice questions.
4. **📝 AI MCQ Quiz Generator**: Interactive quiz player with timer, question navigation, immediate explanations, and score tracking saved to SQLite DB.
5. **🔬 Prompt Lab & Engineering (HERO FEATURE)**: Analyzes weak prompts, displays a visual score gauge (0-100), highlights 6-dimension weaknesses, generates improved prompts, and allows live execution testing.
6. **🚀 Career & Skill Roadmap**: 4-phase technical roadmap generator with portfolio project blueprints and target certifications based on degree and target career.
7. **✅ Academic Task Manager**: Coursework task board with priority badges, overdue alerts, filter tabs, and completion toggles.
8. **📈 Progress Analytics**: Tracks quiz history, study streaks, and subject mastery rates.

---

## 🛠️ Tech Stack

- **Frontend**: React 18, Vite, Tailwind CSS (Custom Dark Navy / Purple / Cyan Palette), Recharts, Lucide React Icons.
- **Backend**: Python 3.14, FastAPI, SQLAlchemy, SQLite Database, Pydantic, HTTPX.
- **AI Integration**: Gemini 2.0 Flash / Gemini 1.5 Flash via REST API with fallback to `MockDataService` for 100% reliable offline hackathon demos.

---

## ⚡ Quick Start & Setup Instructions

### 1. Prerequisites
- Python 3.10+ installed
- Node.js 18+ and npm installed

### 2. Backend Setup
```bash
cd backend
python -m pip install -r requirements.txt
```

Create `.env` file inside `backend/`:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```
*(Note: If no API key is set, StudyPilot AI automatically activates high-quality mock fallbacks so the app remains fully functional offline!)*

Run backend server:
```bash
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```
Backend API will be live at `http://127.0.0.1:8000` (Health Check: `http://127.0.0.1:8000/health`).

### 3. Frontend Setup
```bash
cd frontend
npm install
npm run dev
```
Frontend Web UI will be live at `http://localhost:5173`.

---

## 🎬 3-Minute Hackathon Demo Flow

1. **0:00 - 0:30 (Dashboard)**: Open `http://localhost:5173`. Highlight Alex's B.Tech Data Science student profile, study activity bar chart, subject mastery radar, and AI Copilot recommendation about Recursion.
2. **0:30 - 1:00 (AI Study Planner)**: Click **Study Planner**. Enter "Machine Learning", topics "Gradient Descent, Loss Functions", Exam Date. Click **Generate AI Study Plan**. Show structured day-by-day timetable and topic priority matrix.
3. **1:00 - 1:30 (AI Tutor & Quiz)**: Click **AI Tutor**. Query "Recursion in Python" at Intermediate level. Show simple analogy, step-by-step logic, code snippet, and practice question. Click **Quiz Generator**, take a 3-question MCQ quiz, answer live, and show score saved to database.
4. **1:30 - 2:15 (Prompt Lab - HERO DEMO)**: Click **Prompt Lab**. Click sample weak prompt: `"make me a machine learning project"`. Click **Analyze Prompt**. Show **42/100 score gauge** and detected weaknesses. Review AI-transformed prompt. Click **Run Improved Prompt** to display the live execution output!
5. **2:15 - 3:00 (Career Roadmap)**: Click **Career Roadmap**. Input target career "AI Engineer". Click **Build Career Roadmap** to display 4-phase milestone timeline, required core skills, and portfolio project blueprints.

---

## 📁 Project Architecture

```
studypilot-ai/
├── backend/
│   ├── main.py                     # FastAPI app initialization, CORS, DB seeding
│   ├── database.py                 # SQLite database engine & SessionLocal
│   ├── models.py                   # SQLAlchemy models (Student, Task, StudyPlan, QuizResult, etc.)
│   ├── schemas.py                  # Pydantic schemas for request/response validation
│   ├── routers/
│   │   ├── dashboard.py            # Summary metrics & recommendations
│   │   ├── planner.py              # Study planner generator
│   │   ├── tutor.py                # AI concept explanations
│   │   ├── quiz.py                 # Quiz generator & submission
│   │   ├── prompt_lab.py           # Prompt evaluation & live test
│   │   ├── career.py               # Career roadmap generator
│   │   └── tasks.py                # Task CRUD endpoints
│   ├── services/
│   │   ├── gemini_service.py       # Centralized Gemini API service
│   │   └── mock_data_service.py    # Offline demo mock data service
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── components/             # Sidebar, Header, CopilotDrawer
│   │   ├── pages/
│   │   │   ├── Dashboard.jsx       # Overview, charts, checklist
│   │   │   ├── StudyPlanner.jsx    # Form & timetable viewer
│   │   │   ├── AITutor.jsx         # Multi-level concept tutor
│   │   │   ├── QuizGenerator.jsx   # Interactive MCQ player
│   │   │   ├── PromptLab.jsx       # Prompt analyzer & score gauge
│   │   │   ├── CareerRoadmap.jsx   # Skill & career roadmap
│   │   │   ├── TaskManager.jsx     # Task board & filters
│   │   │   └── ProgressTracker.jsx # Subject mastery & quiz history
│   │   ├── services/api.js         # Axios API endpoints client
│   │   ├── App.jsx                 # App routing & tab layout
│   │   ├── index.css               # Tailwind CSS custom styles
│   │   └── main.jsx
│   ├── package.json
│   ├── vite.config.js
│   └── tailwind.config.js
└── README.md
```
