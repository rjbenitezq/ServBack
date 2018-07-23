from django.db import models

PERSONA_ESTADO_CHOICES = (
    ('A', 'activo'),
    ('I', 'inactivo'),
)


# Create your models here.
class Persona(models.Model):
    # personaCod = models.CharField(max_length=20, unique=True)
    personaNombres = models.CharField(max_length=50)
    personaApellidos = models.CharField(max_length=50)
    personaDni = models.CharField(max_length=8, null=True)
    personaTelefono = models.CharField(max_length=9, null=True)
    personaEmail = models.EmailField()
    personaEstado = models.CharField(max_length=1, null=True)
