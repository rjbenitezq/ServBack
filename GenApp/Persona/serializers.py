from rest_framework import serializers

from GenApp.Persona.models import Persona


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('id',
                  'personaNombres',
                  'personaApellidos',
                  'personaDni',
                  'personaTelefono',
                  'personaEmail',
                  'personaEstado')
