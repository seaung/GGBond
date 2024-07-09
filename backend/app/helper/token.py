from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

from typing import Union


def create_token(data: dict, expires_delta: Union[timedelta, None] = None):
    pass


