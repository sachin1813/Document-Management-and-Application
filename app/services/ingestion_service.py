import shutil, os
from sqlalchemy.orm import Session
from app.models.document import Document
from app.schemas.document import DocumentUpdate
from datetime import datetime
from app.config import settings
from fastapi import HTTPException
from app.utility.genrateFileName import generateFileName
from uuid import UUID
from app.models.ingestion import Ingestion
from app.utility import threaded
import time
import threading


def trigger_ingestion_service(createdData,db):
    document = db.query(Document).filter(Document.doc_id == createdData.doc_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")
    # Create an ingestion record and set status to QUEUED
    ingestion = Ingestion(
        doc_id=document.doc_id,
        status="QUEUED",
        triggered_by=createdData.trigger_by,
        created_at=datetime.now(),
        updated_at=datetime.now(),
    )
    db.add(ingestion)
    db.commit()
    # Now set status to IN_PROGRESS,SUCCESS,FAILURE BY CALLING THREAD (you can change this once actual ingestion starts)
    thread = threading.Thread(target=threaded.threaded_ingestion, args=(ingestion.job_id,))
    thread.start()

    return {"message": "Ingestion started", "doc_title": str(document.title), "status": "QUEUED"}

def trigger_getAll_ingestion_service(db):
    ingestion = db.query(Ingestion).all()
    return {"status":200,"indgestion":ingestion}

def trigger_update_ingestion_service(db,update_data):
    if not update_data.status:
        raise HTTPException(status_code=400, detail=f"Status is madatory to modify:")
    ingestion = db.query(Ingestion).filter(Ingestion.job_id == update_data.job_id).first()
    ingestion.status = update_data.status
    db.commit()
    db.refresh(ingestion)
    return {"status_code":200,"message":"updated successfully !"}

    