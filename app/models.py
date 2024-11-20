from sqlalchemy import Column, Integer, String, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.dialects.postgresql import JSON, TSVECTOR
from app.database import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    full_text_search = Column(TSVECTOR, index=True)
    uploaded_at = Column(String, nullable=False)

class QuizTemplate(Base):
    __tablename__ = "quiz_templates"
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(Integer, ForeignKey("documents.id"), nullable=False)
    questions = Column(JSON, nullable=False)
    difficulty = Column(String, nullable=False)
    name = Column(String, nullable=False)
    topic = Column(String, nullable=False)
    file_ids = Column(ARRAY(String), nullable=False) 
    number_of_questions = Column(Integer, nullable=True) 


class QuizAttempt(Base):
    __tablename__ = "quiz_attempts"
    id = Column(Integer, primary_key=True, index=True)
    quiz_template_id = Column(Integer, ForeignKey("quiz_templates.id"), nullable=False)
    user_answers = Column(JSON, nullable=False)
    is_passed = Column(Boolean, default=False)
