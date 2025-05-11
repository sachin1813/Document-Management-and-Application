import time
from sqlalchemy.orm import Session
from app.models.ingestion import Ingestion
from app.database import SessionLocal
from datetime import datetime
from fastapi import HTTPException


def threaded_ingestion(job_id):
    # Create a new DB session in thread
    db: Session = SessionLocal()
    try:
        ingestion = db.query(Ingestion).filter(Ingestion.job_id==job_id).first()
        if ingestion:
            ingestion.status = "IN_PROGRESS"
            ingestion.updated_at = datetime.now()
            db.commit()
            time.sleep(20)
            try:
                # Call your actual ingestion logic here
                # For example: process_data(document)
                
                # If ingestion is successful
                ingestion.status = "SUCCESS"
                ingestion.updated_at = datetime.now()
                db.commit()
                return {"message": "Ingestion successful", "process_id": ingestion.job_id}
            
            except Exception as e:
                # If an error occurs during ingestion
                ingestion.status = "FAILURE"
                ingestion.updated_at = datetime.now()
                ingestion.error_message = str(e)  #  error message for debugging
                db.commit()
                raise HTTPException(status_code=500, detail=f"Ingestion failed: {str(e)}")
    finally:
        db.close()
