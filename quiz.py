from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import json
from database import get_db
import models
import schemas
from services.gemini_service import gemini_service

router = APIRouter(prefix="/api/quiz", tags=["quiz"])

@router.post("/generate", response_model=schemas.QuizGenerateResponse)
def generate_quiz(req: schemas.QuizRequest):
    return gemini_service.generate_quiz(
        subject=req.subject,
        topic=req.topic,
        difficulty=req.difficulty,
        num_questions=req.num_questions
    )

@router.post("/submit")
def submit_quiz(req: schemas.QuizSubmitRequest, db: Session = Depends(get_db)):
    percentage = round((req.score / req.total_questions) * 100, 1) if req.total_questions > 0 else 0
    
    db_result = models.QuizResult(
        student_id=1,
        subject=req.subject,
        topic=req.topic,
        difficulty=req.difficulty,
        score=req.score,
        total_questions=req.total_questions,
        percentage=percentage,
        result_json=json.dumps({
            "user_answers": req.user_answers,
            "questions": [q.dict() for q in req.questions]
        })
    )
    db.add(db_result)

    # Increment student mastered topics if score >= 80%
    student = db.query(models.Student).filter(models.Student.id == 1).first()
    if student and percentage >= 80:
        student.mastered_topics = min(student.total_topics, student.mastered_topics + 1)
    
    db.commit()
    db.refresh(db_result)

    return {
        "status": "success",
        "result_id": db_result.id,
        "score": req.score,
        "total": req.total_questions,
        "percentage": percentage,
        "feedback": "Outstanding performance! Mastery unlocked!" if percentage >= 80 else "Good effort! Review the explanations to achieve full mastery."
    }

@router.get("/history")
def get_quiz_history(db: Session = Depends(get_db)):
    results = db.query(models.QuizResult).filter(models.QuizResult.student_id == 1).order_by(models.QuizResult.id.desc()).all()
    return [
        {
            "id": r.id,
            "subject": r.subject,
            "topic": r.topic,
            "difficulty": r.difficulty,
            "score": r.score,
            "total_questions": r.total_questions,
            "percentage": r.percentage,
            "created_at": r.created_at.strftime("%Y-%m-%d %H:%M") if r.created_at else "Recently"
        }
        for r in results
    ]
