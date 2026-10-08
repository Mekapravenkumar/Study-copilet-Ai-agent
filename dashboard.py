from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import json
from database import get_db
import models
import schemas
from services.mock_data_service import MockDataService

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])

@router.get("/summary")
def get_dashboard_summary(db: Session = Depends(get_db)):
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
        db.refresh(student)

    tasks = db.query(models.Task).filter(models.Task.student_id == 1).all()
    completed_tasks = [t for t in tasks if t.is_completed]
    overdue_tasks = [t for t in tasks if not t.is_completed and "Yesterday" in t.deadline]
    upcoming_tasks = [t for t in tasks if not t.is_completed][:3]

    quiz_results = db.query(models.QuizResult).filter(models.QuizResult.student_id == 1).order_by(models.QuizResult.id.desc()).all()
    avg_score = round(sum(q.percentage for q in quiz_results) / len(quiz_results), 1) if quiz_results else 78.5

    # Subject performance chart data
    subject_performance = [
        {"subject": "Python", "score": 88, "target": 95},
        {"subject": "Machine Learning", "score": 75, "target": 90},
        {"subject": "Statistics", "score": 82, "target": 85},
        {"subject": "Data Structures", "score": 68, "target": 85}
    ]

    # Weekly study hours chart data
    weekly_hours = [
        {"day": "Mon", "hours": 4.5, "target": 4.0},
        {"day": "Tue", "hours": 6.0, "target": 4.0},
        {"day": "Wed", "hours": 5.0, "target": 4.0},
        {"day": "Thu", "hours": 7.5, "target": 4.0},
        {"day": "Fri", "hours": 3.5, "target": 4.0},
        {"day": "Sat", "hours": 8.0, "target": 5.0},
        {"day": "Sun", "hours": 8.0, "target": 5.0}
    ]

    return {
        "student": {
            "id": student.id,
            "name": student.name,
            "degree": student.degree,
            "semester": student.semester,
            "target_career": student.target_career,
            "total_study_hours": student.total_study_hours,
            "mastered_topics": student.mastered_topics,
            "total_topics": student.total_topics,
            "avg_quiz_score": avg_score
        },
        "task_counts": {
            "total": len(tasks),
            "completed": len(completed_tasks),
            "pending": len(tasks) - len(completed_tasks),
            "overdue": len(overdue_tasks)
        },
        "upcoming_tasks": [
            {"id": t.id, "title": t.title, "subject": t.subject, "deadline": t.deadline, "priority": t.priority, "is_completed": t.is_completed}
            for t in upcoming_tasks
        ],
        "subject_performance": subject_performance,
        "weekly_hours": weekly_hours,
        "ai_recommendations": MockDataService.get_dashboard_recommendations()
    }
