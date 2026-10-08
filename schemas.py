from pydantic import BaseModel, Field
from typing import List, Optional, Any, Dict

# Student Profile
class StudentResponse(BaseModel):
    id: int
    name: str
    degree: str
    semester: int
    target_career: str
    total_study_hours: float
    mastered_topics: int
    total_topics: int

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    degree: Optional[str] = None
    semester: Optional[int] = None
    target_career: Optional[str] = None

# Tasks
class TaskCreate(BaseModel):
    title: str
    subject: str
    deadline: str
    priority: str = "Medium"

class TaskResponse(BaseModel):
    id: int
    student_id: int
    title: str
    subject: str
    deadline: str
    priority: str
    is_completed: bool

class TaskStatusUpdate(BaseModel):
    is_completed: bool

# Study Planner
class StudyPlanRequest(BaseModel):
    subject: str
    topics: List[str]
    exam_date: str
    current_level: str = "Intermediate" # Beginner, Intermediate, Advanced
    hours_per_day: int = 3
    study_style: str = "Pomodoro"       # Pomodoro, Visual, Active Recall, Deep Work

class StudyPlanResponse(BaseModel):
    id: Optional[int] = None
    subject: str
    exam_date: str
    strategy_overview: str
    priority_topics: List[Dict[str, Any]]
    daily_schedule: List[Dict[str, Any]]
    revision_plan: List[str]
    exam_prep_tips: List[str]

# AI Tutor
class TutorRequest(BaseModel):
    topic: str
    level: str = "Intermediate" # Beginner, Intermediate, Advanced
    subject: Optional[str] = None

class TutorResponse(BaseModel):
    topic: str
    level: str
    simple_explanation: str
    step_by_step: List[str]
    code_example: str
    common_mistakes: List[str]
    practice_question: Dict[str, Any] # { question, answer }

# AI Quiz Generator
class QuizRequest(BaseModel):
    subject: str
    topic: str
    difficulty: str = "Medium" # Easy, Medium, Hard
    num_questions: int = 5

class QuizQuestion(BaseModel):
    id: int
    question: str
    options: List[str]
    correct_answer: int # Index 0..3
    explanation: str

class QuizGenerateResponse(BaseModel):
    subject: str
    topic: str
    difficulty: str
    questions: List[QuizQuestion]

class QuizSubmitRequest(BaseModel):
    subject: str
    topic: str
    difficulty: str
    score: int
    total_questions: int
    user_answers: List[int]
    questions: List[QuizQuestion]

# Prompt Lab / Improver
class PromptAnalysisRequest(BaseModel):
    prompt: str

class PromptAnalysisResponse(BaseModel):
    original_prompt: str
    score: int # 0-100
    metrics: Dict[str, int] # clarity, context, specificity, constraints, output_format, audience
    problems: List[str]
    suggestions: List[str]
    improved_prompt: str
    why_better: List[str]

class TestPromptRequest(BaseModel):
    prompt: str

# Career Roadmap
class CareerRoadmapRequest(BaseModel):
    degree: str = "B.Tech Data Science"
    current_skills: List[str]
    target_career: str = "AI Engineer"
    experience_level: str = "Beginner"

class CareerRoadmapResponse(BaseModel):
    degree: str
    target_career: str
    overview: str
    timeline_phases: List[Dict[str, Any]]
    core_skills: List[str]
    portfolio_projects: List[Dict[str, Any]]
    target_certifications: List[str]
