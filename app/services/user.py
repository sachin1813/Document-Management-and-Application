from sqlalchemy.orm import Session
from app.models.user import User
from app.models.userRoles import UserRoles
from app.schemas.user import UserCreate,UserUpdate
from app.utility import EncDec
from fastapi import  HTTPException

def create_user(db: Session, user_data: UserCreate):
    #password encryption
    hashed_pwd = EncDec.hash_password(user_data.password)

    #insertion object
    db_user = User(
        username=user_data.username,
        login_id=user_data.login_id,
        password=hashed_pwd,  
        name=user_data.name,
        user_type=user_data.user_type.upper(),
        status= 'Y'
    )

    addToDb(db_user,db)
    #object creation of insertion in user_roles
    db_user_roles = UserRoles(
        user_id = db_user.user_id,
        role_code = user_data.role_code
    )

    addToDb(db_user_roles,db)
    return {"response" : "User Added Successfully ","status_code" : 200}

def addToDb(Users,db):
    #insertion of object to databse
    db.add(Users)
    db.commit()

    #fetch users_id in return
    db.refresh(Users)
    return Users

def fetchAllUsers(db,userStatus):
    status = userStatus.upper()
    if status == "ALL":
        users = db.query(User).all()
    else:
        users = db.query(User).filter(User.status == userStatus).all()
    return {"users" : users,"status_code" : 200 }

def updateUser(db,updated_data:UserUpdate,user_id):
    user = db.query(User).filter(User.user_id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if updated_data.user_type:
        user.user_type = updated_data.user_type
    if updated_data.status:
        user.status = updated_data.status
    if updated_data.role:
        updateRoles(db,updated_data,user_id)
    db.commit()
    db.refresh(user)
    return {"message": "User updated", "user": user,"status_code" : 200}

def updateRoles(db,updated_data,user_id):
    user_roles = db.query(User).filter(User.user_id == user_id).first()
    if not user_roles:
        raise HTTPException(status=404,detail="user roles not found")
    user_roles.role_code = updated_data.role
    db.commit()
    db.refresh(user_roles)
    return user_roles