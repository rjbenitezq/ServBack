from django.db import models
from GenApp.Categoria.models import Categoria


class Producto(models.Model):
    productoCod = models.CharField(max_length=15, unique=True)
    productoNombre = models.CharField(max_length=50)
    productoDescripcion = models.CharField(max_length=50)
    productoPrecio = models.FloatField(default=None)
    productoEstado = models.CharField(max_length=1)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)


class Combustible(models.Model):
    combustibleCod = models.CharField(max_length=15, unique=True)
    combustibleNombre = models.CharField(max_length=50)
    combustibleDescripcion = models.CharField(max_length=80)
    combustiblePrecioUnidad = models.FloatField()
    combustibleEstado = models.CharField(max_length=1)
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
