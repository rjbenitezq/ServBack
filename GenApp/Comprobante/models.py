from django.db import models

from GenApp.Cliente.models import Cliente
from GenApp.Producto.models import Producto, Combustible
from GenApp.Promocion.models import Promocion
from GenApp.Sucursal.models import Sucursal
from GenApp.Trabajador.models import Trabajador


class Comprobante(models.Model):
    comprobanteCod = models.CharField(max_length=15, unique=True)
    combrobanteCantidad = models.FloatField()
    comprobanteTotal = models.FloatField()
    comprobanteFecha = models.DateTimeField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    trabajador = models.ForeignKey(Trabajador, on_delete=models.PROTECT)
    promocion = models.ForeignKey(Promocion, on_delete=models.PROTECT, blank=True)
    producto = models.ManyToManyField(Producto, blank=True)
    combustible = models.ForeignKey(Combustible, on_delete=models.PROTECT, blank=True)

# class Bitacora(models.Model):
#   comprobante = models.ForeignKey(Comprobante, on_delete=models.PROTECT)
