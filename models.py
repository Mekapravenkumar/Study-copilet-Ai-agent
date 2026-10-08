from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, Float, ForeignKey
from sqlalchemy.sql import func
from database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    degree = Column(String(100), nullable=False)
    semester = Column(Integer, default=5)
    target_career = Column(String(100), default="AI Engineer")
    total_study_hours = Column(Float, default=42.5)
    mastered_topics = Column(Integer, default=18)
    total_topics = Column(Integer, default=24)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), default=1)
    title = Column(String(200), nullable=False)
    subject = Column(String(100), nullable=False)
    deadline = Column(String(50), nullable=False)
    priority = Column(String(20), default="Medium")  # High, Medium, Low
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class StudyPlan(Base):
    __tablename__ = "study_plans"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), default=1)
    subject = Column(String(100), nullable=False)
    topics = Column(Text, nullable=False)
    exam_date = Column(String(50), nullable=False)
    current_level = Column(String(50), default="Intermediate")
    hours_per_day = Column(Integer, default=3)
    study_style = Column(String(50), default="Pomodoro")
    plan_json = Column(Text, nullable=False)  # JSON payload of the generated schedule
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class QuizResult(Base):
    __tablename__ = "quiz_results"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), default=1)
    subject = Column(String(100), nullable=False)
    topic = Column(String(100), nullable=False)
    difficulty = Column(String(20), default="Medium")
    score = Column(Integer, nullable=False)
    total_questions = Column(Integer, nullable=False)
    percentage = Column(Float, nullable=False)
    result_json = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class PromptEvaluation(Base):
    __tablename__ = "prompt_evaluations"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), default=1)
    original_prompt = Column(Text, nullable=False)
    score = Column(Integer, nullable=False)
    evaluation_json = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class CareerRoadmap(Base):
    __tablename__ = "career_roadmaps"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), default=1)
    degree = Column(String(100), nullable=False)
    target_career = Column(String(100), nullable=False)
    roadmap_json = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
