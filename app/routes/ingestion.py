from fastapi import APIRouter, Depends
from app.database import get_db
from uuid import UUID
from sqlalchemy.orm import Session
from app.services import ingestion_service
from app.schemas.ingestion import IngestionUpdate,Ingestion

router = APIRouter()

@router.post("/ingest/trigger")
def trigger_ingestion(creationData:Ingestion, db: Session = Depends(get_db)):
    return ingestion_service.trigger_ingestion_service(creationData,db)

@router.get("/ingest/all")
def trigger_getAll_ingestion(db: Session = Depends(get_db)):
    return ingestion_service.trigger_getAll_ingestion_service(db)

@router.post("/ingestupdate/")
def trigger_update_ingestion(updated_data:IngestionUpdate,db: Session = Depends(get_db)):
    return ingestion_service.trigger_update_ingestion_service(db,updated_data)