from typing import Any
from tortoise import models, fields

from app.types.user import pwd_context


class User(models.Model):
    username = fields.CharField(max_length=20, null=False, description="用户名")
    password = fields.CharField(max_length=128, null=False, description="密码")
    nickname = fields.CharField(max_length=20, null=True, description="昵称")
    email = fields.CharField(max_length=50, null=True, description="邮箱")
    phone = fields.CharField(max_length=20, null=True, description="手机号")
    role = fields.CharField(max_length=20, default="user", description="用户角色")
    is_active = fields.BooleanField(default=True, description="是否被激活")
    is_superuser = fields.BooleanField(default=False, description="是否为超级用户")
    is_locked = fields.BooleanField(default=False, description="是否被锁定")
    login_attempts = fields.IntField(default=0, description="登录尝试次数")
    last_login = fields.DatetimeField(null=True, description="最后登录时间")
    password_reset_time = fields.DatetimeField(null=True, description="密码重置时间")
    created_at = fields.DatetimeField(auto_now_add=True, description="创建时间")
    updated_at = fields.DatetimeField(auto_now=True, description="更新时间")

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(raw_password: str) -> str:
        return pwd_context.hash(raw_password)

    @staticmethod
    async def get_user(username: str) -> Optional["User"]:
        try:
            user = await User.filter(username=username).first()
            return user
        except Exception as e:
            logger.error(f"Error fetching user {username}: {str(e)}")
            return None

    @staticmethod
    async def authenticate_user(username: str, password: str) -> bool:
        user = await User.get_user(username)
        if not user:
            return False
        if not User.verify_password(password, user.password):
            return False
        await User.update_login_status(user)
        return True

    @staticmethod
    async def update_login_status(user: "User") -> None:
        user.last_login = datetime.now()
        user.login_attempts = 0
        await user.save()

    @staticmethod
    async def reset_password(user: "User", new_password: str) -> bool:
        try:
            user.password = User.get_password_hash(new_password)
            user.password_reset_time = datetime.now()
            await user.save()
            return True
        except Exception as e:
            logger.error(f"Error resetting password for user {user.username}: {str(e)}")
            return False

    def __str__(self) -> str:
        return self.username

    def __repr__(self) -> str:
        return '<User : %s>' % self.username

    class Meta:
        table = 'users'

