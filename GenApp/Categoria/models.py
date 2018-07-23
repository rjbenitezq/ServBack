from django.db import models


# Create your models here.

class Categoria(models.Model):
    categoriaCod = models.CharField(max_length=15, unique=True)
    categoriaNombre = models.CharField(max_length=50)
    categoriaDescripcion = models.CharField(max_length=80)
    categoriaFiltro = models.CharField(max_length=1)
    categoriaEstado = models.CharField(max_length=1)
