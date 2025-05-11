from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from uuid import UUID

class DocumentBase(BaseModel):
    title: str
    description: Optional[str] = None
    file_path: str
    status: Optional[str] = 'Y'  # 'Y' for active, 'N' for inactive
    uploaded_by: int

class DocumentCreate(DocumentBase):
    pass

class DocumentUpdate(BaseModel):
    title: Optional[str]
    description: Optional[str]

class DocumentOut(DocumentBase):
    title: str
    description: Optional[str]
    file_path: str
    status: Optional[str]
    uploaded_by: UUID
    doc_id: UUID

    class Config:
        orm_mode = True

    