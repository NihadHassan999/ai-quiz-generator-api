from pydantic import BaseModel
from typing import List, Optional

class QuizCreate(BaseModel):
    name: str
    difficulty: str
    topic: str
    file_ids: List[str]
    number_of_questions: Optional[int] = None  # Make this optional
    question_type: Optional[str] = None       # Make this optional
    custom_instructions: Optional[str] = None

class QuizSubmission(BaseModel):
    answers: List[dict]
