from rest_framework import serializers

from GenApp.Privilegios.models import Privilegios, Roles


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ('rolesViatura', 'modulos')


class PrivilegioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Privilegios
        fields = ('id',
                  'privilegioDescripcion',
                  'privilegioRecurso',
                  'privilegioDependencia',
                  'privilegioEstado',
                  'privilegioIcono',
                  'modulos')
