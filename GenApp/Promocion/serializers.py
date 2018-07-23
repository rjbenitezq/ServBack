from rest_framework import serializers

from GenApp.Promocion.models import Promocion, Motivo, PromocionVale, PromocionDescuento
from GenApp.Sucursal.models import Sucursal


class PromocionValeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromocionVale
        fields = ('id', 'promocionValeCod', 'promocionValeNombre')


class PromocionDescuentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromocionDescuento
        fields = ('id', 'descuentoCod', 'descuentoPorcentaje')


class MotivosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motivo
        fields = ('id',
                  'motivoCod',
                  'motivoNombre',
                  'motivoTipo',
                  'ConsumoMonto',
                  'ConsumoVeces')


class SucursalProSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = ('id', 'sucursalDescripcion')


class MotivosProSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motivo
        fields = ('id', 'motivoNombre')


class PromocionSerializer(serializers.ModelSerializer):
    motivo = MotivosProSerializer(write_only=False, read_only=True)
    sucursal = SucursalProSerializer(many=True, write_only=False, read_only=True)
    promocionVale = PromocionValeSerializer(write_only=False, many=False, read_only=True)
    promocionDescuento = PromocionDescuentoSerializer(write_only=False, read_only=True)

    class Meta:
        model = Promocion
        fields = ('id',
                  'promocionCod',
                  'promocionNombre',
                  'promocionDescripcion',
                  'promocionInicio',
                  'promocionFin',
                  'promocionTipoC',
                  'sucursal',
                  'promocionVale',
                  'promocionDescuento',
                  'motivo',
                  'imagen',
                  'promocionEstado')

    def create(self, validated_data):
        titulares_data = self.initial_data.get('sucursal')
        tracks_motivo = self.initial_data.get('motivo')
        tracks_vale = self.initial_data.get('promocionVale')
        tracks_descuento = self.initial_data.get('promocionDescuento')
        tracks_promocionCod = validated_data.pop('promocionCod')
        tracks_promocionNombre = validated_data.pop('promocionNombre')
        tracks_promocionDescripcion = validated_data.pop('promocionDescripcion')
        tracks_promocionInicio = validated_data.pop('promocionInicio')
        tracks_promocionFin = validated_data.pop('promocionFin')
        tracks_promocionTipoC = validated_data.pop('promocionTipoC')
        tracks_promocionEstado = validated_data.pop('promocionEstado')
        if tracks_descuento is not None:
            recipe = Promocion.objects.create(promocionCod=tracks_promocionCod,
                                              promocionNombre=tracks_promocionNombre,
                                              promocionDescripcion=tracks_promocionDescripcion,
                                              promocionInicio=tracks_promocionInicio,
                                              promocionFin=tracks_promocionFin,
                                              promocionTipoC=tracks_promocionTipoC,
                                              promocionEstado=tracks_promocionEstado,
                                              motivo_id=tracks_motivo['id'],
                                              promocionDescuento_id=tracks_descuento['id'])
            for titulares in titulares_data:
                for titu in titulares:
                    recipe.sucursal.add(titu['id'])
        if tracks_vale is not None:
            recipe = Promocion.objects.create(promocionCod=tracks_promocionCod,
                                              promocionNombre=tracks_promocionNombre,
                                              promocionDescripcion=tracks_promocionDescripcion,
                                              promocionInicio=tracks_promocionInicio,
                                              promocionFin=tracks_promocionFin,
                                              promocionTipoC=tracks_promocionTipoC,
                                              promocionEstado=tracks_promocionEstado,
                                              motivo_id=tracks_motivo['id'],
                                              promocionVale_id=tracks_vale['id'])
            for titulares in titulares_data:
                for titu in titulares:
                    recipe.sucursal.add(titu['id'])
        return recipe
