from fastapi import APIRouter, Depends
from app.services.analytics_service import get_quiz_analytics, get_user_analytics
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.get("/quiz/{quiz_id}")
async def get_quiz_analytics_endpoint(quiz_id: str, start_date: str, end_date: str, db: Session = Depends(get_db)):
    analytics = get_quiz_analytics(quiz_id, start_date, end_date, db)
    return analytics

@router.get("/user/{user_id}")
async def get_user_analytics_endpoint(user_id: str, db: Session = Depends(get_db)):
    analytics = get_user_analytics(user_id, db)
    return analytics
