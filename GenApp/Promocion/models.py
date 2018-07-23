from django.db import models

from GenApp.Sucursal.models import Sucursal


class PromocionVale(models.Model):
    promocionValeCod = models.CharField(max_length=15, unique=True)
    promocionValeNombre = models.CharField(max_length=50)


class PromocionDescuento(models.Model):
    descuentoCod = models.CharField(max_length=15, unique=True)
    descuentoPorcentaje = models.FloatField()


class Motivo(models.Model):
    motivoCod = models.CharField(max_length=15, unique=True)
    motivoNombre = models.CharField(max_length=50)
    motivoTipo = models.CharField(max_length=1, null=True, blank=True)
    ConsumoMonto = models.FloatField(blank=True)
    ConsumoVeces = models.IntegerField(blank=True)


class Promocion(models.Model):
    promocionCod = models.CharField(max_length=15, unique=True)
    promocionNombre = models.CharField(max_length=50)
    promocionDescripcion = models.CharField(max_length=80)
    promocionInicio = models.DateTimeField()
    promocionFin = models.DateTimeField()
    promocionTipoC = models.CharField(max_length=1)
    sucursal = models.ManyToManyField(Sucursal)
    promocionVale = models.ForeignKey(PromocionVale, on_delete=models.CASCADE, null=True)
    promocionDescuento = models.ForeignKey(PromocionDescuento, on_delete=models.CASCADE, null=True)
    motivo = models.ForeignKey(Motivo, on_delete=models.CASCADE, null=True)
    habilitar = models.CharField(max_length=1, null=True)
    publicar = models.CharField(max_length=1, null=True)
    imagen = models.CharField(max_length=800, null=True, blank=True)
    promocionEstado = models.CharField(max_length=1)
