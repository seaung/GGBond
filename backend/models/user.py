from tortoise import models, fields


class User(models.Model):
    username = fields.CharField(max_length=20, null=False, description="用户名")
    password = fields.CharField(max_length=128, null=False, description="密码")
    nickname = fields.CharField(max_length=20, null=True, description="昵称")




