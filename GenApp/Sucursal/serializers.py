from rest_framework import serializers

from GenApp.Sucursal.models import Sucursal


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('id',
                  'sucursalCod',
                  'sucursalDescripcion',
                  'sucursalDireccion',
                  'sucursalReferencia',
                  'sucursalLatitud',
                  'sucursalLongitud')
