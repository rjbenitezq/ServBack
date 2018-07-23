from django.db import models

# Create your models here.


class Sucursal(models.Model):
    sucursalCod = models.CharField(max_length=15, unique=True)
    sucursalDescripcion = models.CharField(max_length=50)
    sucursalDireccion = models.CharField(max_length=80)
    sucursalReferencia = models.CharField(max_length=80)
    sucursalLatitud = models.CharField(max_length=50)
    sucursalLongitud = models.CharField(max_length=50)