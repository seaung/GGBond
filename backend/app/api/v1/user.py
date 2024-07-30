from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
from starlette.status import HTTP_403_FORBIDDEN
from starlette.requests import Request

from app.types.user import UserLoginRequestForm


user_bp = APIRouter(prefix='/user')


@user_bp.post(path="/access_token", summary="token用户登录")
async def login_access_token(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    pass


@user_bp.post(path="/login", summary="用户正常登录逻辑")
async def login(request: Request, login_form: UserLoginRequestForm):
    username:str = login_form.username
    password:str = login_form.password

