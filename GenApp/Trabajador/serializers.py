from rest_framework import serializers
from django.contrib.auth.models import User

from GenApp.Cargo.serializers import CargoSerializer
from GenApp.Persona.serializers import PersonaSerializer
from GenApp.Trabajador.models import Trabajador


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

class TrabajadorSerializer(serializers.ModelSerializer):
    persona = PersonaSerializer(many=False, read_only=True)
    usuario = UsuarioSerializer()
    cargo =  CargoSerializer()

    class Meta:
        model = Trabajador
        fields = ('id','trabajadorCod','trabajadorEstado','persona','cargo', 'usuario')