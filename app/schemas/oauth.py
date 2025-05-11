from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class UserOAuthCreate(BaseModel):
    user_id: UUID
    login_id: str
    token: str
    logged_in: bool = True
    expires_in: datetime