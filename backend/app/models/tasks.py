from datetime import datetime
from tortoise import models, fields


class TaskModel(models.Model):
    id = fields.BigIntField(primary_key=True)
    uuid = fields.CharField(max_length=128, null=False, unique=False, description='任务id')
    target = fields.CharField(max_length=128, null=False, description='目标地址')
    name = fields.CharField(max_length=50, null=False, description='任务名称')
    itype = fields.CharField(max_length=30, null=False, description='任务类型')
    status = fields.IntField(null=False, description='任务状态')
    created_at = fields.DatetimeField(default=datetime.now, description='创建日期')
    updated_at = fields.DatetimeField(default=datetime.now, description='更新日期')

