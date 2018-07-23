from django.db import models

TIPOVEHICULO_ESTADO_CHOICES = (
    ('A', 'activo'),
    ('I', 'inactivo'),
)


# Create your models here.

class TipoVehiculo(models.Model):
    tipovehiculoCod = models.CharField(max_length=15, unique=True)
    tipovehiculoDescripcion = models.CharField(max_length=50)
    tipovehiculoEstado = models.CharField(max_length=1, choices=TIPOVEHICULO_ESTADO_CHOICES)
