from django.db import models

from GenApp.Area.models import Area


# Create your models here.
class Cargo(models.Model):
    cargoCod = models.CharField(max_length=20, unique=True)
    cargoDescripcion = models.CharField(max_length=80)
    area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True, blank=True)
