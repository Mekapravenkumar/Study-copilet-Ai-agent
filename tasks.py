from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
import models
import schemas

router = APIRouter(prefix="/api/tasks", tags=["tasks"])

@router.get("", response_model=List[schemas.TaskResponse])
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).filter(models.Task.student_id == 1).order_by(models.Task.id.desc()).all()

@router.post("", response_model=schemas.TaskResponse)
def create_task(req: schemas.TaskCreate, db: Session = Depends(get_db)):
    db_task = models.Task(
        student_id=1,
        title=req.title,
        subject=req.subject,
        deadline=req.deadline,
        priority=req.priority,
        is_completed=False
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_task_status(task_id: int, req: schemas.TaskStatusUpdate, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.is_completed = req.is_completed
    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"status": "success", "message": "Task deleted"}
