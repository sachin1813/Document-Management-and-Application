from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserLogin
from app.services.auth import loginService

router = APIRouter()

@router.post("/login")
def login(user_login: UserLogin, db: Session = Depends(get_db)):
    return loginService(user_login,db)