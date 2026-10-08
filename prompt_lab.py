from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import json
from database import get_db
import models
import schemas
from services.gemini_service import gemini_service

router = APIRouter(prefix="/api/prompt-lab", tags=["prompt_lab"])

@router.post("/analyze", response_model=schemas.PromptAnalysisResponse)
def analyze_prompt(req: schemas.PromptAnalysisRequest, db: Session = Depends(get_db)):
    result = gemini_service.analyze_prompt(req.prompt)
    
    # Save evaluation to database
    db_eval = models.PromptEvaluation(
        student_id=1,
        original_prompt=req.prompt,
        score=result["score"],
        evaluation_json=json.dumps(result)
    )
    db.add(db_eval)
    db.commit()

    return result

@router.post("/test")
def test_improved_prompt(req: schemas.TestPromptRequest):
    """Executes the improved prompt live in Gemini API or fallback to demonstrate the quality difference."""
    explanation = gemini_service.generate_tutor_explanation(topic=req.prompt, level="Advanced")
    return {
        "status": "success",
        "output_type": "Structured Project & Concept Blueprint",
        "result": explanation
    }
