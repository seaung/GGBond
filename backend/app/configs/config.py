import os.path

from pydantic import BaseConfig

# 当前目录
CURRENT_DIR = os.path.abspath(__file__)


# 项目根目录
ROOT_PATH = os.path.dirname(os.path.dirname(CURRENT_DIR))


class Settings(BaseConfig):
    class Config:
        env_file = '.env'

    DEBUG: bool = True

    SECRET_KEY: str = ''

    TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    TOKEN_ALGORITHM: str = 'HS256'

    DB_NAME: str = 'rs_db'

    DB_PORT: int = 5432

    DB_HOST: str = '0.0.0.0'

    DB_USER: str = 'rs_db'

    DB_PASS: str = 'rs_db@123456'


settings = Settings()

