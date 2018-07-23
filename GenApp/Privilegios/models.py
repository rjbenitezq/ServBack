from django.contrib.auth.models import User
from django.db import models


class Modulos(models.Model):
    moduloNCod = models.CharField(max_length=45)
    moduloNombre = models.CharField(max_length=45)

    def __str__(self):
        return '{}'.format(self.moduloNombre)


class ModUser(models.Model):
    modulos = models.ForeignKey(Modulos, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)


class Roles(models.Model):
    rolesNCod = models.CharField(max_length=45)
    rolesNombre = models.CharField(max_length=45)
    rolesViatura = models.CharField(max_length=10, unique=True)
    modulos = models.ForeignKey(Modulos, on_delete=models.PROTECT)

    def __str__(self):
        return '{}'.format(self.rolesNombre)


class RolUser(models.Model):
    roles = models.ForeignKey(Roles, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return '{}'.format(self.roles)


class Privilegios(models.Model):
    privilegioDescripcion = models.CharField(max_length=80)
    privilegioRecurso = models.CharField(max_length=150)
    privilegioDependencia = models.IntegerField()
    privilegioEstado = models.CharField(max_length=1)
    privilegioIcono = models.CharField(max_length=60)
    modulos = models.ForeignKey(Modulos, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return '{}'.format(self.privilegioDescripcion)
