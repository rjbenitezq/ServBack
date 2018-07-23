from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView
from GenApp.TipoVehiculo.models import TipoVehiculo
from GenApp.TipoVehiculo.serializers import TipoVehiculoSerializer


class ListTipoVehiculo(APIView):

    def get(self, request):
        tipovehiculo = TipoVehiculo.objects.all()
        serializer = TipoVehiculoSerializer(tipovehiculo, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TipoVehiculoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)