from django.shortcuts import render
from django.http import Http404
import random

from rest_framework import status
from rest_framework.response import Response

from rest_framework.views import APIView
from GenApp.Area.models import Area
from GenApp.Area.serializers import AreaSerializer


class ListArea(APIView):

    def get(self, request):
        area = Area.objects.all()
        serializer = AreaSerializer(area, many=True)
        return Response(serializer.data)

    def post(self, request):
        tro = random.randint(100000, 900000)
        num = random.randint(97, 122)
        pep = random.randint(97, 122)
        varo = chr(num).upper() + chr(pep).upper() + str(tro)
        vale = Area.objects.filter(areaCod=varo).count()
        while vale < 1:
            request.data["areaCod"] = varo
            serializer = AreaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListAreaDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    # permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Area.objects.get(pk=pk)
        except Area.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bus = self.get_object(pk)
        serializer = AreaSerializer(bus)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bus = self.get_object(pk)
        serializer = AreaSerializer(bus, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        bus = self.get_object(pk)
        bus.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
