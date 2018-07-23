from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from GenApp.Privilegios.models import Privilegios, RolUser, Roles, ModUser, Modulos
from GenApp.Privilegios.serializers import PrivilegioSerializer, RolesSerializer


class RolesList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        a = request.user.id
        user = User.objects.get(id=a)
        rol_user = RolUser.objects.filter(user=user.id)
        roles = Roles.objects.filter(id__in=rol_user)
        serializer = RolesSerializer(roles, many=True)
        return Response(serializer.data)


class OpcionesList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        a = request.user.id
        modu_qs = ModUser.objects.filter(user=a).values_list('modulos', flat=True)
        vmodulo = Modulos.objects.filter(id__in=list(modu_qs))
        opcion = Privilegios.objects.filter(Q(modulos__in=vmodulo) | Q(privilegioRecurso='#'))
        serializer = PrivilegioSerializer(opcion, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PrivilegioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
