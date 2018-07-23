from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView
from GenApp.Trabajador.models import Trabajador
from GenApp.Trabajador.serializers import TrabajadorSerializer


class ListTrabajador(APIView):

    def get(self, request):
        trabajador = Trabajador.objects.all()
        serializer = TrabajadorSerializer(trabajador, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = TrabajadorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListTrabajadorDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    #permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Trabajador.objects.get(pk=pk)
        except Trabajador.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bus = self.get_object(pk)
        serializer = TrabajadorSerializer(bus)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bus = self.get_object(pk)
        serializer = TrabajadorSerializer(bus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bus = self.get_object(pk)
        bus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)