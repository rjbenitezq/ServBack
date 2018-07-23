import random

from django.http import Http404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from rest_framework.views import APIView
from GenApp.Cliente.models import Cliente
from GenApp.Cliente.serializers import ClienteSerializer
from GenApp.Persona.models import Persona
from GenApp.Persona.serializers import PersonaSerializer


class ListCliente(APIView):
    permission_classes = (AllowAny,)

    def get(self, request):
        cliente = Cliente.objects.all()
        serializer = ClienteSerializer(cliente, many=True)
        return Response(serializer.data)

    def post(self, request):
        tro = random.randint(100000, 900000)
        num = random.randint(97, 122)
        pep = random.randint(97, 122)
        varo = chr(num).upper() + chr(pep).upper() + str(tro)
        body = request.data
        if body["tipoCliente"] == 'N':
            data = {
                "clienteCod": varo,
                "clienteAbrev": "N",
                "persona": {'personaNombres': body["nombre"],
                            'personaApellidos': body["apellidos"],
                            'personaEmail': body["correo"]
                            },
                "juridico": '',
                "usuario": {
                    'username': body["usuario"],
                    'password': body["password1"]
                }
            }
        if body["tipoCliente"] == 'J':
            data = {
                "clienteCod": varo,
                "clienteAbrev": "J",
                "juridico": {'juridicoRazonSocial': body["nombre"],
                             'juridicoRUC': body["ruc"],
                             'juridicoEmail': body["correo"]
                             },
                "usuario": {
                    'username': body["usuario"],
                    'password': body["password1"]
                }
            }
        serializer = ClienteSerializer(data=data)

        print(request.data)
        if serializer.is_valid():
            print("pase")
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListClienteDetail(APIView):
    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bus = self.get_object(pk)
        serializer = ClienteSerializer(bus)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bus = self.get_object(pk)
        serializer = ClienteSerializer(bus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bus = self.get_object(pk)
        bus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DataPersonalClienteApp(APIView):

    def get(self, request):
        idd = request.user.id
        cliente = Cliente.objects.get(id=idd)
        persona = Persona.objects.get(id=cliente.persona.pk)
        serializer = PersonaSerializer(persona)
        return Response(serializer.data)
