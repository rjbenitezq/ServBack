from rest_framework import serializers

from GenApp.Producto.models import Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ('id',
                  'productoCod',
                  'productoNombre',
                  'productoDescripcion',
                  'productoPrecio',
                  'productoEstado',
                  'categoria')
