from tortoise import models, fields


class Results(models.Model):
    id = fields.IntField(primary_key=True)
    ip = fields.CharField(null=False)
    port = fields.CharField(null=False)
    devices = fields.CharField(null=False)

