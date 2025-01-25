import os
from typing import Optional
from functools import lru_cache

from pydantic import BaseConfig, Field

# 当前目录
CURRENT_DIR = os.path.abspath(__file__)

# 项目根目录
ROOT_PATH = os.path.dirname(os.path.dirname(CURRENT_DIR))

class Settings(BaseConfig):
    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        case_sensitive = True

    # 基础配置
    ENV: str = Field('dev', env='ENV')
    DEBUG: bool = Field(True, env='DEBUG')
    SECRET_KEY: str = Field('your-super-secret-key-here', env='SECRET_KEY')
    
    # Token配置
    TOKEN_EXPIRE_MINUTES: int = Field(60 * 24 * 8, env='TOKEN_EXPIRE_MINUTES')
    TOKEN_ALGORITHM: str = Field('HS256', env='TOKEN_ALGORITHM')
    
    # 数据库配置
    DB_NAME: str = Field('rs_db', env='DB_NAME')
    DB_PORT: int = Field(5432, env='DB_PORT')
    DB_HOST: str = Field('0.0.0.0', env='DB_HOST')
    DB_USER: str = Field('rs_db', env='DB_USER')
    DB_PASS: str = Field('rs_db@123456', env='DB_PASS')
    
    @property
    def DATABASE_URL(self) -> str:
        return f"postgresql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    
    # Redis配置
    REDIS_HOST: str = Field('localhost', env='REDIS_HOST')
    REDIS_PORT: int = Field(6379, env='REDIS_PORT')
    REDIS_DB: int = Field(0, env='REDIS_DB')
    REDIS_PASSWORD: Optional[str] = Field(None, env='REDIS_PASSWORD')
    
    @property
    def REDIS_URL(self) -> str:
        if self.REDIS_PASSWORD:
            return f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"
    
    # 日志配置
    LOG_LEVEL: str = Field('INFO', env='LOG_LEVEL')
    LOG_FORMAT: str = Field('%(asctime)s - %(name)s - %(levelname)s - %(message)s', env='LOG_FORMAT')
    LOG_FILE: Optional[str] = Field(None, env='LOG_FILE')

@lru_cache()
def get_settings() -> Settings:
    """获取配置单例
    
    Returns:
        Settings: 配置实例
    """
    return Settings()

settings = get_settings()

