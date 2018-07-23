from rest_framework import serializers

from GenApp.Juridico.models import Juridico


class JuridicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Juridico
        fields = ('id','juridicoCod','juridicoRazonSocial','juridicoRUC','juridicoEmail')