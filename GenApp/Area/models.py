from django.db import models

from GenApp.Sucursal.models import Sucursal


class Area(models.Model):
    areaCod = models.CharField(max_length=20, unique=True)
    areaDescripcion = models.CharField(max_length=80, unique=True)
    areaEstado = models.CharField(max_length=1)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT, null=True)
