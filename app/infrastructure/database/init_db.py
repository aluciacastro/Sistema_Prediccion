# backend/app/infrastructure/database/init_db.py
from app.infrastructure.database.connection import get_engine
from app.infrastructure.database.models import Base

def init_db():
    engine = get_engine()
    Base.metadata.create_all(bind=engine)
    print("✅ Tablas creadas correctamente.")

if __name__ == "__main__":
    init_db()
