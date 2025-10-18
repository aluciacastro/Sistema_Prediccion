# backend/app/infrastructure/database/connection.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

# ✅ Base declarativa para los modelos
Base = declarative_base()

# ✅ Configuración del motor de base de datos
_engine = create_engine(settings.DATABASE_URL, future=True)
_SessionLocal = sessionmaker(bind=_engine, autocommit=False, autoflush=False)

# ✅ Dependencia para obtener la sesión en endpoints
def get_db_session():
    return _SessionLocal()

# ✅ Devuelve el motor (para crear tablas o migraciones)
def get_engine():
    return _engine
