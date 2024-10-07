from typing import Any
from tortoise import models, fields

from app.types.user import pwd_context


class User(models.Model):
    username = fields.CharField(max_length=20, null=False, description="用户名")
    password = fields.CharField(max_length=128, null=False, description="密码")
    nickname = fields.CharField(max_length=20, null=True, description="昵称")
    is_active = fields.BooleanField(default=True, description="是否被激活")
    is_superuser = fields.BooleanField(default=False, description="是否为超级用户")

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(raw_password: str) -> str:
        return pwd_context.hash(raw_password)

    def get_user(self, username: str) -> Any:
        user = User.filter(username=username).first().prefetch_related()
        if user:
            return user

    @staticmethod
    def authenticate_user(username: str, password: str) -> bool:
        user = User.filter(username=username).first().prefetch_related()
        if not user:
            return False
        if not verify_password(password, user.password):
            return False
        return True

    def __str__(self) -> str:
        return self.username

    def __repr__(self) -> str:
        return '<User : %s>' % self.username

    class Meta:
        table = 'users'

