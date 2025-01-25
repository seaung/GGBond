from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter, Depends
from starlette.status import HTTP_403_FORBIDDEN
from starlette.requests import Request

from app.types.user import UserLoginRequestForm
from app.models.user import User
from app.helper.token import create_token
from app.types.user import oauth2_scheme
from app.types.response import ResponseModel


user_bp = APIRouter(prefix='/user')


@user_bp.post(path="/access_token", summary="token用户登录")
async def login_access_token(request: Request, form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    user = await User.get_user(username)
    if not user:
        return ResponseModel.forbidden("用户不存在").json_response()
    
    if user.is_locked:
        return ResponseModel.forbidden("账户已被锁定，请联系管理员").json_response()

    if not user.is_active:
        return ResponseModel.forbidden("账户未激活").json_response()

    ok = await User.authenticate_user(username=username, password=password)
    if not ok:
        user.login_attempts += 1
        if user.login_attempts >= 5:
            user.is_locked = True
        await user.save()
        return ResponseModel.forbidden("用户名或密码错误").json_response()

    data = {
        "username": username,
        "uuid": user.id
    }
    token = create_token(data=data)
    return ResponseModel.success({
        "access_token": token,
        "token_type": "bearer"
    }).json_response()


@user_bp.post(path="/login", summary="用户正常登录逻辑")
async def login(request: Request, login_form: UserLoginRequestForm):
    username: str = login_form.username
    password: str = login_form.password

    user = await User.get_user(username)
    if not user:
        return ResponseModel.forbidden("用户不存在").json_response()
    
    if user.is_locked:
        return ResponseModel.forbidden("账户已被锁定，请联系管理员").json_response()

    if not user.is_active:
        return ResponseModel.forbidden("账户未激活").json_response()

    ok = await User.authenticate_user(username=username, password=password)
    if not ok:
        user.login_attempts += 1
        if user.login_attempts >= 5:
            user.is_locked = True
        await user.save()
        return ResponseModel.forbidden("用户名或密码错误").json_response()

    data = {
        "username": username,
        "uuid": user.id
    }
    token = create_token(data=data)
    return ResponseModel.success({
        "access_token": token,
        "token_type": "bearer"
    }).json_response()


@user_bp.get("/info", summary="获取当前用户信息")
async def get_current_user_info(request: Request, token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.TOKEN_ALGORITHM])
        username = payload.get("username")
        if not username:
            return ResponseModel.forbidden("无效的token").json_response()
        
        user = await User.get_user(username)
        if not user:
            return ResponseModel.not_found("用户不存在").json_response()
            
        return ResponseModel.success({
            "id": user.id,
            "username": user.username,
            "nickname": user.nickname,
            "email": user.email,
            "phone": user.phone,
            "role": user.role,
            "is_active": user.is_active,
            "is_superuser": user.is_superuser,
            "last_login": user.last_login,
            "created_at": user.created_at
        }).json_response()
    except jwt.PyJWTError:
        return ResponseModel.forbidden("无效的token").json_response()

@user_bp.put("/info", summary="更新用户信息")
async def update_user_info(request: Request, token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.TOKEN_ALGORITHM])
        username = payload.get("username")
        if not username:
            return ResponseModel.forbidden("无效的token").json_response()
            
        user = await User.get_user(username)
        if not user:
            return ResponseModel.not_found("用户不存在").json_response()
            
        data = await request.json()
        allowed_fields = ["nickname", "email", "phone"]
        
        for field in allowed_fields:
            if field in data:
                setattr(user, field, data[field])
                
        await user.save()
        return ResponseModel.success(msg="用户信息更新成功").json_response()
    except jwt.PyJWTError:
        return ResponseModel.forbidden("无效的token").json_response()
    except ValueError as e:
        return ResponseModel.error(str(e)).json_response()

