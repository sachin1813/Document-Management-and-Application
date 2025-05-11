from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserLogin
from app.models.user import User
from app.database import get_db
from app.utility import EncDec
from app.utility.token import create_access_token
from app.models.oauth import UserOAuth
from datetime import datetime, timedelta
from app.config import settings
from app.query.postgresQry import fetchUserRoles


def loginService(user_login: UserLogin, db: Session = Depends(get_db)):
    #VALIDATING THE lOGIN_ID AND PASSWORD 
    user = db.query(User).filter(User.login_id == user_login.login_id).first()
    if not user or not EncDec.verify_password(user_login.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    #If login success generate token session
    token = create_access_token(data={"sub": user.login_id})

    #storing the token generated in database mapped with user details
    oauth_entry = UserOAuth(
        user_id=user.user_id,
        login_id=user.login_id,
        token=token,
        logged_in=datetime.now(),
        expires_in=datetime.now() + timedelta(seconds=settings.JWT_EXPIRATION_SECONDS)  # or your desired expiry
    )

    db.add(oauth_entry)
    db.commit()
    db.refresh(oauth_entry)

    role = getRoles(db,user)

    
    return {"access_token": token, "token_type": "bearer", "roles" : role, "user_id" : user.user_id}

def getRoles(db,user):
    fetchRolesquery = fetchUserRoles()
    userRoles = db.execute(fetchRolesquery, {"user_id": user.user_id})
    for role in userRoles:
        return role[0]
