from sqlalchemy import Column, String, Integer, DateTime, Text, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Document(Base):
    __tablename__ = "documents"

    doc_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    file_path = Column(String, nullable=False)
    status = Column(String(1), default='Y')  # 'Y' for active, 'N' for inactive
    uploaded_by = Column(Integer, ForeignKey("users.user_id"), nullable=False)  # Assuming 'users' table exists
    upload_time = Column(DateTime(timezone=True), server_default=func.now())
