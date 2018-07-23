from rest_framework import serializers

from GenApp.Categoria.models import Categoria


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = ('id',
                  'categoriaCod',
                  'categoriaNombre',
                  'categoriaDescripcion',
                  'categoriaFiltro',
                  'categoriaEstado')
