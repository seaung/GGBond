from fastapi import APIRouter


user_bp = APIRouter(prefix='/user')


@user_bp.post(path="/login", summary="用户登录")
async def login():
    pass

