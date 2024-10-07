from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
from starlette.status import HTTP_403_FORBIDDEN
from starlette.requests import Request

from app.types.user import UserLoginRequestForm
from app.models.user import User
from app.helper.token import create_token


user_bp = APIRouter(prefix='/user')


@user_bp.post(path="/access_token", summary="token用户登录")
async def login_access_token(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    pass


@user_bp.post(path="/login", summary="用户正常登录逻辑")
async def login(request: Request, login_form: UserLoginRequestForm):
    username:str = login_form.username
    password:str = login_form.password

    ok: bool = User.authenticate_user(username=username, password=password)
    if ok:
        data = {
                'username': username,
        }
        token = create_token(data=data)
        token_data = {
                'msg': 'ok',
                'access_token': token,
                'code': 200
        }
        return token_data
    return {'msg': 'error', 'code': HTTP_403_FORBIDDEN}

