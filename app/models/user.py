from sqlalchemy import Column, Integer, String
from app.database import Base


class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    login_id = Column(String)
    password = Column(String)
    name = Column(String)
    user_type = Column(String)
    status = Column(String, default="Y")