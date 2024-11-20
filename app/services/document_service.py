from app.models import Document
from sqlalchemy.orm import Session

def upload_document(file, db: Session):
    new_document = Document(filename=file.filename, content=file.file.read().decode())
    db.add(new_document)
    db.commit()
    return new_document.id

def search_documents(q: str, page: int, limit: int, sort: str, file_type: str, db: Session):
    # Implement full-text search logic
    return []

def get_file_by_id(file_id: str, db: Session):
    return db.query(Document).filter(Document.id == file_id).first()
