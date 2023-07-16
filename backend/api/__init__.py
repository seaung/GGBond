from fastapi import APIRouter

from api.v1.api import api_bp
from api.v1.user import user_bp


api_route = APIRouter()

api_route.include_router(api_bp, prefix="/v1", tags=["api相关"])
api_route.include_router(user_bp, prefix="/user/v1", tags=["用户相关API"])

