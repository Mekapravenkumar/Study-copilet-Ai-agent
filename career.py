from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import json
from database import get_db
import models
import schemas
from services.gemini_service import gemini_service

router = APIRouter(prefix="/api/career", tags=["career"])

@router.post("/roadmap", response_model=schemas.CareerRoadmapResponse)
def generate_career_roadmap(req: schemas.CareerRoadmapRequest, db: Session = Depends(get_db)):
    roadmap = gemini_service.generate_career_roadmap(
        degree=req.degree,
        current_skills=req.current_skills,
        target_career=req.target_career,
        experience_level=req.experience_level
    )

    db_roadmap = models.CareerRoadmap(
        student_id=1,
        degree=req.degree,
        target_career=req.target_career,
        roadmap_json=json.dumps(roadmap)
    )
    db.add(db_roadmap)
    db.commit()

    return roadmap
