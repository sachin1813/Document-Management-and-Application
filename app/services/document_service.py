import shutil, os
from sqlalchemy.orm import Session
from app.models.document import Document
from app.schemas.document import DocumentUpdate
from datetime import datetime
from app.config import settings
from fastapi import HTTPException
from app.utility.genrateFileName import generateFileName
from uuid import UUID
from fastapi.responses import FileResponse


def create_document(file, title, description, uploaded_by, db: Session):
    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)
    new_file_name = generateFileName(file.filename)
    file_path = os.path.join(settings.UPLOAD_DIR, new_file_name)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    document = Document(
        title=title,
        description=description,
        file_path=file_path,
        uploaded_by=uploaded_by,
        upload_time=datetime.now(),
        status="Y"
    )
    db.add(document)
    db.commit()
    db.refresh(document)
    return document


def get_all_documents(db: Session):
    documents = db.query(Document).all()
    if not documents:
        raise HTTPException(status_code=200, detail="No documents found")
    return {"status_code" : 200,"document":documents}


def get_document_by_title(title: str, db: Session):
    document =  db.query(Document).filter(Document.title == title).all()
    return {"status_code":200,"document" : document}

def update_document(doc_id: UUID, updated_data: DocumentUpdate, db: Session):
    doc = get_document_by_id(doc_id, db)
    if not doc:
        return None

    if updated_data.title:
        doc.title = updated_data.title
    if updated_data.description:
        doc.description = updated_data.description

    db.commit()
    db.refresh(doc)
    return doc


def delete_document(doc_id: int, db: Session):
    doc = get_document_by_id(doc_id, db)
    if not doc:
        return False
    db.delete(doc)
    db.commit()
    if os.path.exists(doc.file_path):
        os.remove(doc.file_path)
    return True

def get_document_by_id(doc_id,db):
    return db.query(Document).filter(Document.doc_id == doc_id).first()

def downloadFile(doc_id,db):
    document = db.query(Document).filter(Document.doc_id == doc_id).first()
    print("sachin ",document.file_path)
    if os.path.exists(document.file_path):
        return FileResponse(path=document.file_path, filename=os.path.basename(document.file_path), media_type='application/octet-stream')
    return {"detail": "File not found"}



