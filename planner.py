from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import json
from database import get_db
import models
import schemas
from services.gemini_service import gemini_service

router = APIRouter(prefix="/api/planner", tags=["planner"])

@router.post("/generate", response_model=schemas.StudyPlanResponse)
def generate_study_plan(req: schemas.StudyPlanRequest, db: Session = Depends(get_db)):
    plan = gemini_service.generate_study_plan(
        subject=req.subject,
        topics=req.topics,
        exam_date=req.exam_date,
        current_level=req.current_level,
        hours_per_day=req.hours_per_day,
        study_style=req.study_style
    )

    # Save plan to database
    db_plan = models.StudyPlan(
        student_id=1,
        subject=req.subject,
        topics=", ".join(req.topics),
        exam_date=req.exam_date,
        current_level=req.current_level,
        hours_per_day=req.hours_per_day,
        study_style=req.study_style,
        plan_json=json.dumps(plan)
    )
    db.add(db_plan)
    db.commit()
    db.refresh(db_plan)

    plan["id"] = db_plan.id
    return plan

@router.get("/latest")
def get_latest_study_plan(db: Session = Depends(get_db)):
    plan = db.query(models.StudyPlan).filter(models.StudyPlan.student_id == 1).order_by(models.StudyPlan.id.desc()).first()
    if not plan:
        # Fallback initial sample plan
        return gemini_service.generate_study_plan(
            subject="Machine Learning",
            topics=["Gradient Descent", "Loss Functions", "Decision Trees"],
            exam_date="2026-10-05",
            current_level="Intermediate",
            hours_per_day=3,
            study_style="Pomodoro"
        )
    return json.loads(plan.plan_json)
