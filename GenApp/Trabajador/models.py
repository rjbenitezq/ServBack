from django.contrib.auth.models import User
from django.db import models

from GenApp.Persona.models import Persona
from GenApp.Cargo.models import Cargo
from GenApp.Sucursal.models import Sucursal


# Create your models here.
class Trabajador(models.Model):
    trabajadorCod = models.CharField(max_length=20, unique=True)
    trabajadorEstado = models.CharField(max_length=1)
    persona = models.OneToOneField(Persona, on_delete=models.PROTECT)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT, null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
