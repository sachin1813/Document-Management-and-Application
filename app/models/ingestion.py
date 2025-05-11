from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Ingestion(Base):
    __tablename__ = "ingestion_jobs"

    job_id = Column(Integer, primary_key=True, index=True)
    triggered_by = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    doc_id = Column(Integer,ForeignKey("documents.doc_id"),nullable=False) # 'document' table
    status = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())
    logs  = Column(String, nullable=False)
    
