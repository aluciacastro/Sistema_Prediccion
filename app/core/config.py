# backend/app/core/config.py
from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    PROJECT_NAME: str = "sistema-desnutricion"
    PROJECT_VERSION: str = "0.1.0"
    API_VERSION: str = "v1"
    DATABASE_URL: str = Field(..., env="DATABASE_URL")
    SECRET_KEY: str = Field(..., env="SECRET_KEY")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 días
    ML_MODELS_PATH: str = "app/infrastructure/ml/models"

    # 👇 Agrega estos dos campos que están en tu .env
    ENVIRONMENT: str = Field("development", env="ENVIRONMENT")
    LOG_LEVEL: str = Field("info", env="LOG_LEVEL")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
