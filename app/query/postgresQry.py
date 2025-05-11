from sqlalchemy import text
from sqlalchemy.orm import Session


def fetchUserRoles():
    query = text("select ur.role_code from user_roles ur ,roles r where ur.role_code = r.role_code and ur.user_id = :user_id")
    return query

