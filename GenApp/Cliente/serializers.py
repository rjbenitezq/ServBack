from django.contrib.auth.models import User
from rest_framework import serializers

from GenApp.Cliente.models import Cliente
from GenApp.Juridico.models import Juridico
from GenApp.Juridico.serializers import JuridicoSerializer
from GenApp.Persona.models import Persona
from GenApp.Persona.serializers import PersonaSerializer


class UsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password')


class ClienteSerializer(serializers.ModelSerializer):
    usuario = UsuarioSerializer(read_only=True)
    persona = PersonaSerializer(read_only=True)
    juridico = JuridicoSerializer(read_only=True)

    class Meta:
        model = Cliente
        fields = ('id', 'clienteCod', 'clienteAbrev', 'persona', 'juridico', 'usuario')

    def create(self, validated_data):
        if validated_data["clienteAbrev"] == 'N':
            tracks_data = self.initial_data.get('usuario')
            tracks_data2 = self.initial_data.get('persona')
            personaN = Persona.objects.create(**tracks_data2)
            usuarioN = User.objects.create_user(**tracks_data)
            cliente = Cliente.objects.create(usuario=usuarioN, persona=personaN, **validated_data)
        if validated_data["clienteAbrev"] == 'J':
            tracks_data = self.initial_data.get('usuario')
            tracks_data2 = self.initial_data.get('juridico')
            personaN = Juridico.objects.create(**tracks_data2)
            usuarioN = User.objects.create_user(**tracks_data)
            cliente = Cliente.objects.create(usuario=usuarioN, juridico=personaN, **validated_data)
        return cliente
