from celery import Celery
from fastapi import FastAPI


def create_celery_app() -> Celery:
    celery_app = Celery('app')

    return celery_app



def create_app() -> FastAPI:
    app = FastAPI()

    app.celery_app = create_celery_app()

    return app

