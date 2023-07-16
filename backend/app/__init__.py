from fastapi import FastAPI



def create_app() -> FastAPI:
    app = FastAPI()

    from api import api_route
    app.include_router(api_route, prefix="/api")
    return app

