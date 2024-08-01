import jwt

from typing import Any, Optional
from datetime import datetime, timedelta
from starlette.requests import Request

from app.configs.config import settings
from app.types.user import Token
from app.models.user import User


def create_token(data: dict, expires_delta: Optional[timedelta] = None) -> Any:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'expire': expire})

    encode_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.TOKEN_ALGORITHM)
    return encode_jwt


def generate_token(request: Request, username: str, password: str) -> Token:
    ...


