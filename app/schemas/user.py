from pydantic import BaseModel
from uuid import UUID

class UserCreate(BaseModel):
    username: str
    login_id: str
    password: str
    name: str
    user_type: str
    role_code: str

class UserOut(BaseModel):
    user_id : UUID
    username: str
    login_id: str
    name: str
    user_type: str
    status: str

    class Config:
        orm_mode = True
    
class UserLogin(BaseModel):
    login_id: str
    password: str

class UserUpdate(BaseModel):
    user_type:str
    status: str 
    role: str

    class Config:
        orm_mode = True