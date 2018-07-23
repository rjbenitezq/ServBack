from rest_framework import serializers

from GenApp.Comprobante.models import Comprobante


class ComprobanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprobante
        fields = ('comprobanteCod',
                  'comprobanteCantidad',
                  'comprobanteFecha',
                  'producto',
                  'combustible',
                  'sucursal',
                  'trabajador',
                  'promocion',
                  'cliente',
                  'comprobanteTotal')