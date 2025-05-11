from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class Ingestion(BaseModel):
    trigger_by : UUID
    doc_id :UUID

    class Config:
        orm_mode = True

class IngestionUpdate(BaseModel):
    job_id:UUID
    status:str

    class config:
        orm_mode = True

class IngestionOut(BaseModel):
    trigger_by : int
    doc_id :int
    status :str
    job_id :int

    class Config:
        orm_mode = True
