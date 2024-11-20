from fastapi import APIRouter, HTTPException, Depends
from app.schemas import QuizCreate, QuizSubmission
from app.services.quiz_service import create_quiz, get_quiz, submit_quiz, get_all_quizzes
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.post("/create")
async def create_quiz_endpoint(payload: QuizCreate, db: Session = Depends(get_db)):
    quiz_id = create_quiz(payload, db)
    return {"quiz_id": quiz_id}

@router.get("/get/{quiz_id}")
async def get_quiz_endpoint(quiz_id: str, db: Session = Depends(get_db)):
    quiz = get_quiz(quiz_id, db)
    if not quiz:
        raise HTTPException(status_code=404, detail="Quiz not found")
    return quiz

@router.post("/{quiz_id}/submit")
async def submit_quiz_endpoint(quiz_id: str, payload: QuizSubmission, db: Session = Depends(get_db)):
    result = submit_quiz(quiz_id, payload, db)
    return {"result": result}

@router.get("/get-all")
async def get_all_quizzes_endpoint(page: int = 1, limit: int = 10, db: Session = Depends(get_db)):
    quizzes = get_all_quizzes(page, limit, db)
    return quizzes
