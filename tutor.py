from fastapi import APIRouter
import schemas
from services.gemini_service import gemini_service

router = APIRouter(prefix="/api/tutor", tags=["tutor"])

@router.post("/explain", response_model=schemas.TutorResponse)
def explain_topic(req: schemas.TutorRequest):
    return gemini_service.generate_tutor_explanation(topic=req.topic, level=req.level)
