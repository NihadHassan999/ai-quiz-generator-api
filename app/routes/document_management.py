from fastapi import APIRouter, HTTPException, Depends, UploadFile
from app.services.document_service import upload_document, search_documents, get_file_by_id
from sqlalchemy.orm import Session
from app.database import get_db

router = APIRouter()

@router.post("/upload")
async def upload_file_endpoint(file: UploadFile, db: Session = Depends(get_db)):
    document_id = upload_document(file, db)
    return {"document_id": document_id}

@router.get("/search")
async def search_files_endpoint(q: str, page: int, limit: int, sort: str, file_type: str, db: Session = Depends(get_db)):
    results = search_documents(q, page, limit, sort, file_type, db)
    return results

@router.get("/{file_id}")
async def get_file_by_id_endpoint(file_id: str, db: Session = Depends(get_db)):
    file = get_file_by_id(file_id, db)
    if not file:
        raise HTTPException(status_code=404, detail="File not found")
    return file
