from app.models import QuizTemplate
from app.schemas import QuizCreate
from sqlalchemy.orm import Session

def create_quiz(payload: QuizCreate, db: Session):
    filtered_payload = payload.dict(exclude={"question_type", "custom_instructions"})
    filtered_payload["document_id"] = 1  # Set a default document ID for testing

    print("Filtered Payload:", filtered_payload)

    new_quiz = QuizTemplate(**filtered_payload)

    db.add(new_quiz)
    db.commit()
    db.refresh(new_quiz)

    print("New Quiz:", new_quiz)
    return new_quiz.id



def get_quiz(quiz_id: str, db: Session):
    return db.query(QuizTemplate).filter(QuizTemplate.id == quiz_id).first()

def submit_quiz(quiz_id: str, payload, db: Session):
    # Validate answers and calculate results (to be implemented)
    return {"status": "submitted"}

def get_all_quizzes(page: int, limit: int, db: Session):
    offset = (page - 1) * limit
    return db.query(QuizTemplate).offset(offset).limit(limit).all()
