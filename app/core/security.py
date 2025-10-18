# backend/app/core/security.py
from datetime import datetime, timedelta
from typing import Optional
import jwt
from app.core.config import settings
from pydantic import BaseModel

class TokenData(BaseModel):
    sub: str
    exp: datetime

def create_access_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    payload = {"sub": subject, "exp": expire}
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)
    return token

def decode_token(token: str) -> TokenData:
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        return TokenData(sub=payload.get("sub"), exp=datetime.fromtimestamp(payload.get("exp")))
    except jwt.PyJWTError as ex:
        raise ValueError("Invalid token") from ex
