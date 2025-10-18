# backend/app/infrastructure/database/connection.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

_engine = create_engine(settings.DATABASE_URL, future=True)
_SessionLocal = sessionmaker(bind=_engine, autocommit=False, autoflush=False)

def get_db_session():
    return _SessionLocal()

def get_engine():
    return _engine
