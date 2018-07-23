from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView
from GenApp.Producto.models import Producto
from GenApp.Producto.serializers import ProductoSerializer


class ListProducto(APIView):

    def get(self, request):
        producto = Producto.objects.all()
        serializer = ProductoSerializer(producto, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
