from rest_framework import serializers

from GenApp.Area.models import Area
from GenApp.Sucursal.models import Sucursal


class SucursalASerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('id', 'sucursalDescripcion')


class AreaSerializer(serializers.ModelSerializer):
    sucursal = SucursalASerializer(write_only=False, read_only=True)

    class Meta:
        model = Area
        fields = ('id',
                  'areaCod',
                  'areaDescripcion',
                  'areaEstado',
                  'sucursal')

    def create(self, validated_data):
        titulares_data = self.initial_data.get('sucursal')
        recipe = Area.objects.create(areaCod=validated_data.pop('areaCod'),
                                     areaDescripcion=validated_data.pop('areaDescripcion'),
                                     areaEstado=validated_data.pop('areaEstado'),
                                     sucursal_id=titulares_data['id'])
        return recipe
