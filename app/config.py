from pydantic_settings import BaseSettings
from typing import ClassVar
from pathlib import Path
import os

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://avnadmin:AVNS_7prEygKyVRAz7aTClq9@docqaplatform-sachin1822singh-2989.h.aivencloud.com:16165/docqaplatform?sslmode=require"
    JWT_SECRET_KEY: str = "7dLQwSFDgHPh4RmHqzvK4uCeH4LM2bR1owACy1u8ZVI"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_SECONDS: int = 3600
    BASE_DIR: ClassVar[Path] = Path(__file__).resolve().parent.parent
    UPLOAD_DIR: ClassVar[Path] = BASE_DIR / "uploads"

    class Config:
        env_file = ".env"

settings = Settings()