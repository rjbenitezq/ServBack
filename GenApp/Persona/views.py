from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView
from GenApp.Persona.models import Persona
from GenApp.Persona.serializers import PersonaSerializer


class ListPersona(APIView):

    def get(self, request):
        persona = Persona.objects.all()
        serializer = PersonaSerializer(persona, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PersonaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListPersonaDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    #permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Persona.objects.get(pk=pk)
        except Persona.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bus = self.get_object(pk)
        serializer = PersonaSerializer(bus)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bus = self.get_object(pk)
        serializer = PersonaSerializer(bus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bus = self.get_object(pk)
        bus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)