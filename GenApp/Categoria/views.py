from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
import random

from rest_framework.views import APIView
from GenApp.Categoria.models import Categoria
from GenApp.Categoria.serializers import CategoriaSerializer


class ListCategoria(APIView):

    def get(self, request):
        categoria = Categoria.objects.all()
        serializer = CategoriaSerializer(categoria, many=True)
        return Response(serializer.data)

    def post(self, request):
        tro = random.randint(100000, 900000)
        num = random.randint(97, 122)
        pep = random.randint(97, 122)
        varo = chr(num).upper() + chr(pep).upper() + str(tro)
        vale = Categoria.objects.filter(categoriaCod=varo).count()
        while vale < 1:
            request.data["categoriaCod"] = varo
            serializer = CategoriaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListCategoriaDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bus = self.get_object(pk)
        serializer = CategoriaSerializer(bus)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bus = self.get_object(pk)
        serializer = CategoriaSerializer(bus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bus = self.get_object(pk)
        bus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
