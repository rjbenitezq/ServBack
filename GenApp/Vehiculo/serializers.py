from rest_framework import serializers

from GenApp.Vehiculo.models import Vehiculo


class VehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehiculo
        fields = ('vehiculoCod','vehiculoPlaca','tipoVehiculo','cliente')