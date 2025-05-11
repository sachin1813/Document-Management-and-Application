from datetime import datetime, timedelta
from jose import JWTError, jwt
from dotenv import load_dotenv
from app.config import settings

load_dotenv()
SECRET_KEY =  settings.JWT_SECRET_KEY
ALGORITHM =  settings.JWT_ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.JWT_EXPIRATION_SECONDS

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(seconds=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)