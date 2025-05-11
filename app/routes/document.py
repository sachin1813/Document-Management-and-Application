from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.document import DocumentOut, DocumentUpdate
from app.services import document_service
from uuid import UUID

router = APIRouter()

@router.post("/", response_model=DocumentOut)
def create(file: UploadFile = File(...), title: str = "", description: str = "", uploaded_by: UUID ="", db: Session = Depends(get_db)):
    return document_service.create_document(file, title, description, uploaded_by, db)


@router.get("/")
def get_all(db: Session = Depends(get_db)):
    return document_service.get_all_documents(db)


@router.get("/{title}")
def get_by_title(title: str, db: Session = Depends(get_db)):
    doc = document_service.get_document_by_title(title, db)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc


@router.put("/{doc_id}", response_model=DocumentOut)
def update(doc_id: UUID, updated_data: DocumentUpdate, db: Session = Depends(get_db)):
    doc = document_service.update_document(doc_id, updated_data, db)
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc


@router.delete("/{doc_id}")
def delete(doc_id: UUID, db: Session = Depends(get_db)):
    success = document_service.delete_document(doc_id, db)
    if not success:
        raise HTTPException(status_code=404, detail="Document not found")
    return {"detail": "Document deleted"}
