from celery import Celery
from fastapi import FastAPI

from app.api.v1 import create_api_v1


def create_celery_app() -> Celery:
    celery_app = Celery('app')

    return celery_app



def create_app() -> FastAPI:
    app = FastAPI()

    app.include_router(router=create_api_v1(), prefix='/api')

    app.celery_app = create_celery_app()

    return app

