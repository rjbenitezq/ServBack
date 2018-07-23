from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView
from GenApp.Vehiculo.models import Vehiculo
from GenApp.Vehiculo.serializers import VehiculoSerializer


class ListVehiculo(APIView):

    def get(self, request):
        vehiculo = Vehiculo.objects.all()
        serializer = VehiculoSerializer(vehiculo, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = VehiculoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)