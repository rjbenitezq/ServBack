from rest_framework import serializers

from GenApp.TipoVegiculo.models import TipoVehiculo


class TipoVehiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoVehiculo
        fields = ('tipovehiculoCod','tipovehiculoDescripcion')