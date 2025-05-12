from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserOut,UserUpdate
from app.services.user import create_user,fetchAllUsers,updateUser
from uuid import UUID


router = APIRouter()

@router.post("/")
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/users/{userStatus}")
def get_all_users(userStatus,db: Session = Depends(get_db)):
    return fetchAllUsers(db,userStatus)

@router.put("/users/{user_id}")
def update_user(user_id: UUID, updated_data: UserUpdate, db: Session = Depends(get_db)):
    return updateUser(db,updated_data,user_id)