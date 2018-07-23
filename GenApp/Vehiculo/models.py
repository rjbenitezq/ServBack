from django.db import models

# Create your models here.
from GenApp.Cliente.models import Cliente
from GenApp.TipoVehiculo.models import TipoVehiculo

class Vehiculo(models.Model):
    vehiculoCod = models.CharField(max_length=15, unique=True)
    vehiculoPlaca = models.CharField(max_length=40, unique=True)
    vehiculoMarca = models.CharField(max_length=20)
    vehiculoModelo = models.CharField(max_length=20)
    tipoVehiculo = models.ForeignKey(TipoVehiculo, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)