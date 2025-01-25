from celery import Celery
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from starlette.middleware.cors import CORSMiddleware

from app.api.v1 import create_api_v1
from app.configs.config import settings


def create_celery_app() -> Celery:
    '''创建celery工厂方法
    return: Celery实例
    '''
    celery_app = Celery('app')
    celery_app.conf.broker_url = 'redis://localhost:6379/0'
    celery_app.conf.result_backend = 'redis://localhost:6379/0'

    return celery_app


def register_db(app: FastAPI) -> None:
    '''注册数据库
    app: FastAPI实例
    return: None
    '''
    db_uri: str = 'sqlite://db.sqlite3'
    tortoise_orm_mapping: dict = {
        'connections': {'default': db_uri},
        'apps': {
            'models': ['app.models.models', 'app.models.user', 'app.models.results'],
            'default_connection': 'default',
        }
    }

    register_tortoise(app, config=tortoise_orm_mapping, generate_schemas=settings.DEBUG)


def register_middlewares(app: FastAPI) -> None:
    '''注册中间件
    app: FastAPI实例
    return: None
    '''
    if settings.DEBUG:
        app.add_middleware(CORSMiddleware, 
            allow_origins=['*'],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=['*'],
        )


def create_app() -> FastAPI:
    '''FastAPI实例工厂方法
    return: FastAPI
    '''
    app = FastAPI()

    register_middlewares(app)
    register_db(app)
    app.include_router(router=create_api_v1(), prefix='/api')
    app.celery_app = create_celery_app()

    return app

