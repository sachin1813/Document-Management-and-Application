from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class UserOAuth(Base):
    __tablename__ = "user_oauth"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    login_id = Column(String, nullable=False)
    token = Column(String, nullable=False)
    logged_in = Column(DateTime, default=datetime.utcnow)
    expires_in = Column(DateTime, default=datetime.utcnow)
