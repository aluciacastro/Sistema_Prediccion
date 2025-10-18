# backend/app/core/dependencies.py
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.core.security import decode_token
from app.infrastructure.database.connection import get_db_session

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        token_data = decode_token(token)
        # In a real app you would look up the user in DB
        return {"id": token_data.sub}
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid auth credentials")

def get_db():
    session = get_db_session()
    try:
        yield session
    finally:
        session.close()
