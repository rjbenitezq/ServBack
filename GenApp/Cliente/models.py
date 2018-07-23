from django.contrib.auth.models import User
from django.db import models

from GenApp.Juridico.models import Juridico
from GenApp.Persona.models import Persona


class Cliente(models.Model):
    clienteCod = models.CharField(max_length=15, unique=True)
    clienteAbrev = models.CharField(max_length=1, null=True)
    persona = models.ForeignKey(Persona, on_delete=models.PROTECT, null=True)
    juridico = models.ForeignKey(Juridico, on_delete=models.PROTECT, null=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
