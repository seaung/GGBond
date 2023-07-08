from tortoise import models
from tortoise import fields


class Search(models.Model):
    coordinates = fields.CharField(max_length=100)
    country = fields.CharField(max_length=100)
    ics = fields.CharField(max_length=100)
    coordinates_search = fields.CharField(max_length=1000)
    nmap = fields.BooleanField(default=False)


class Device(models.Model):
    search = fields.ForeignKeyField(model_name="models.Search", on_delete=fields.CASCADE)
    ip = fields.CharField(max_length=100, default="")
    product = fields.CharField(max_length=500, default="")
    org = fields.CharField(max_length=100, default="", null=True)
    data = fields.CharField(max_length=1000, default="")
    port = fields.CharField(max_length=10, default="")
    type = fields.CharField(max_length=100, default="")
    city = fields.CharField(max_length=100, default="", null=True)
    lon = fields.CharField(max_length=100, default="")
    country_code = fields.CharField(max_length=100, default="")
    query = fields.CharField(max_length=100, default="")
    category = fields.CharField(max_length=100, default="")
    vulns = fields.CharField(max_length=100, default="")
    indicator = fields.CharField(max_length=100, default="")
    hostnames = fields.CharField(max_length=100, default="")
    screenshot = fields.CharField(max_length=100000, default="")
    located = fields.BooleanField(default=False, null=True)
    notes = fields.CharField(max_length=100, default="")
    scan = fields.CharField(max_length=100000, default="")
    exploit = fields.CharField(max_length=10000, default="")
    exploit_scanned = fields.BooleanField(default=False)


class DeviceNearby(models.Model):
    device = fields.ForeignKeyField("models.Device", on_delete=fields.CASCADE)
    lat = fields.CharField(max_length=100)
    lon = fields.CharField(max_length=100)
    ip = fields.CharField(max_length=100)
    product = fields.CharField(max_length=100)
    port = fields.CharField(max_length=100)
    org = fields.CharField(max_length=100)
