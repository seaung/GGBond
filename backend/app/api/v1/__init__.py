from fastapi.routing import APIRouter

from app.api.v1.api import api_bp
from app.api.v1.user import user_bp


def create_api_v1() -> APIRouter:

    routers = APIRouter(prefix='/v1')

    routers.include_router(api_bp)
    routers.include_router(user_bp)
    return routers


