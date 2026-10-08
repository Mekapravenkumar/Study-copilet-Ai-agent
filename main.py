import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

from database import engine, Base, SessionLocal
import models
from routers import dashboard, planner, tutor, quiz, prompt_lab, career, tasks

# Initialize Database tables
Base.metadata.create_all(bind=engine)

def seed_demo_data():
    db = SessionLocal()
    try:
        student = db.query(models.Student).filter(models.Student.id == 1).first()
        if not student:
            student = models.Student(
                id=1,
                name="Alex",
                degree="B.Tech Data Science",
                semester=5,
                target_career="AI Engineer",
                total_study_hours=42.5,
                mastered_topics=18,
                total_topics=24
            )
            db.add(student)
            db.commit()

        # Seed initial tasks if empty
        task_count = db.query(models.Task).count()
        if task_count == 0:
            sample_tasks = [
                models.Task(student_id=1, title="Review Python Recursion & Stack Traces", subject="Python", deadline="Today, 6:00 PM", priority="High", is_completed=False),
                models.Task(student_id=1, title="Complete Machine Learning Gradient Descent Lab", subject="Machine Learning", deadline="Tomorrow, 11:59 PM", priority="High", is_completed=False),
                models.Task(student_id=1, title="Read Probability Distributions Chapter 4", subject="Statistics", deadline="In 3 days", priority="Medium", is_completed=False),
                models.Task(student_id=1, title="Submit Binary Search Tree Assignment", subject="Data Structures", deadline="Yesterday", priority="High", is_completed=False),
                models.Task(student_id=1, title="Prepare Prompt Engineering Presentation", subject="AI Engineering", deadline="In 5 days", priority="Low", is_completed=True)
            ]
            db.add_all(sample_tasks)

        # Seed initial quiz result if empty
        quiz_count = db.query(models.QuizResult).count()
        if quiz_count == 0:
            sample_quizzes = [
                models.QuizResult(student_id=1, subject="Python", topic="Recursion", difficulty="Medium", score=3, total_questions=5, percentage=60.0),
                models.QuizResult(student_id=1, subject="Machine Learning", topic="Supervised Learning", difficulty="Medium", score=4, total_questions=5, percentage=80.0),
                models.QuizResult(student_id=1, subject="Statistics", topic="Hypothesis Testing", difficulty="Hard", score=5, total_questions=5, percentage=100.0)
            ]
            db.add_all(sample_quizzes)

        db.commit()
    finally:
        db.close()

seed_demo_data()

app = FastAPI(
    title="StudyPilot AI Backend",
    description="AI Student Copilot Backend Service for PromptWars X HackArena",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(dashboard.router)
app.include_router(planner.router)
app.include_router(tutor.router)
app.include_router(quiz.router)
app.include_router(prompt_lab.router)
app.include_router(career.router)
app.include_router(tasks.router)

@app.get("/health")
def health_check():
    return {
        "status": "online",
        "app": "StudyPilot AI",
        "gemini_api_configured": bool(os.getenv("GEMINI_API_KEY"))
    }
