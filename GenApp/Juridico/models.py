from django.db import models


# Create your models here.


class Juridico(models.Model):
    juridicoCod = models.CharField(max_length=15, null=True)
    juridicoRazonSocial = models.CharField(max_length=50, null=True)
    juridicoRUC = models.CharField(max_length=11, null=True)
    juridicoEmail = models.EmailField(null=True)
