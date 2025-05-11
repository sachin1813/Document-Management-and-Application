from sqlalchemy import Column, Integer, String
from app.database import Base
from uuid import UUID


class UserRoles(Base):
    __tablename__ = "user_roles"
    user_id = Column(Integer, primary_key=True,index=True)
    role_code = Column(String,primary_key=True,index=True)
    