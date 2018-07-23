from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView
from GenApp.Comprobante.models import Comprobante
from GenApp.Comprobante.serializers import ComprobanteSerializer


class ListComprobante(APIView):

    def get(self, request):
        comprobante = Comprobante.objects.all()
        serializer = ComprobanteSerializer(comprobante, many = True)
        return Response(serializer.data)

    def post(self,request):
        serializer = ComprobanteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)