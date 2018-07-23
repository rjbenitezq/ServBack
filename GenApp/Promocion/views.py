from django.http import Http404
import random
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import datetime, timedelta, time
from rest_framework.views import APIView

from GenApp.Cliente.models import Cliente
from GenApp.Promocion.serializers import *
from GenApp.Sucursal.models import Sucursal


class ListPromocionVale(APIView):

    def get(self, request):
        promocionVale = PromocionVale.objects.all()
        serializer = PromocionValeSerializer(promocionVale, many=True)
        return Response(serializer.data)

    def post(self, request):
        tro = random.randint(100000, 900000)
        num = random.randint(97, 122)
        pep = random.randint(97, 122)
        varo = chr(num).upper() + chr(pep).upper() + str(tro)
        vale = PromocionVale.objects.filter(promocionValeCod=varo).count()
        while vale < 1:
            request.data["promocionValeCod"] = varo
            serializer = PromocionValeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListPromocionValesDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return PromocionVale.objects.get(pk=pk)
        except PromocionVale.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        vale = self.get_object(pk)
        serializer = PromocionValeSerializer(vale)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        vale = self.get_object(pk)
        serializer = PromocionValeSerializer(vale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        vale = self.get_object(pk)
        vale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListPromocionDescuento(APIView):

    def get(self, request):
        promocionDescuento = PromocionDescuento.objects.all()
        serializer = PromocionDescuentoSerializer(promocionDescuento, many=True)
        return Response(serializer.data)

    def post(self, request):

        tro = random.randint(100000, 900000)
        num = random.randint(97, 122)
        pep = random.randint(97, 122)
        varo = chr(num).upper() + chr(pep).upper() + str(tro)
        vale = PromocionDescuento.objects.filter(descuentoCod=varo).count()
        while vale < 1:
            request.data["descuentoCod"] = varo
            serializer = PromocionDescuentoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListPromocionDescuentoDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return PromocionDescuento.objects.get(pk=pk)
        except PromocionDescuento.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        descuento = self.get_object(pk)
        serializer = PromocionDescuentoSerializer(descuento)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        descuento = self.get_object(pk)
        serializer = PromocionDescuentoSerializer(descuento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        descuento = self.get_object(pk)
        descuento.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListMotivos(APIView):

    def get(self, request):
        motivo = Motivo.objects.all()
        serializer = MotivosSerializer(motivo, many=True)
        return Response(serializer.data)

    def post(self, request):
        tro = random.randint(100000, 900000)
        num = random.randint(97, 122)
        pep = random.randint(97, 122)
        varo = chr(num).upper() + chr(pep).upper() + str(tro)
        vale = Motivo.objects.filter(motivoCod=varo).count()
        while vale < 1:
            request.data["motivoCod"] = varo
            serializer = MotivosSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListMotivosDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Motivo.objects.get(pk=pk)
        except Motivo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        motivo = self.get_object(pk)
        serializer = MotivosSerializer(motivo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        descuento = self.get_object(pk)
        serializer = MotivosSerializer(descuento, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        motivo = self.get_object(pk)
        motivo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListPromocion(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        promocion = Promocion.objects.all()
        serializer = PromocionSerializer(promocion, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        tro = random.randint(100000, 900000)
        num = random.randint(97, 122)
        pep = random.randint(97, 122)
        varo = chr(num).upper() + chr(pep).upper() + str(tro)
        vale = Promocion.objects.filter(promocionCod=varo).count()
        while vale < 1:
            request.data["promocionCod"] = varo
            serializer = PromocionSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListPromocionQueEs(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        idd = request.user.id
        conta = Cliente.objects.get(usuario_id=idd)
        if (conta.clienteAbrev == 'N'):
            today = datetime.now().date()
            today_inicio = datetime.combine(today, time())
            print(today_inicio)
            promocion = Promocion.objects.order_by('id').exclude(promocionInicio__gte=today_inicio).exclude(
                promocionFin__lt=today_inicio).filter(
                promocionFin__gte=today_inicio).filter(promocionTipoC='N')
            serializer = PromocionSerializer(promocion, many=True)
            return Response(serializer.data)
        if (conta.clienteAbrev == 'J'):
            today = datetime.now().date()
            today_inicio = datetime.combine(today, time())
            print(today_inicio)
            promocion = Promocion.objects.order_by('id').exclude(promocionInicio__gte=today_inicio).filter(
                promocionFin__gte=today_inicio).filter(promocionTipoC='J')
            serializer = PromocionSerializer(promocion, many=True)
            return Response(serializer.data)


class ListSucursalPro(APIView):

    def get(self, request):
        sucursal = Sucursal.objects.all()
        serializer = SucursalProSerializer(sucursal, many=True)
        return Response(serializer.data)


class ListMotivoPro(APIView):

    def get(self, request):
        motivo = Motivo.objects.all()
        serializer = MotivosProSerializer(motivo, many=True)
        return Response(serializer.data)
