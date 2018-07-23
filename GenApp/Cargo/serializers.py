from rest_framework import serializers

from GenApp.Area.serializers import AreaSerializer
from GenApp.Cargo.models import Cargo



class CargoSerializer(serializers.ModelSerializer):
    area = AreaSerializer()
    class Meta:
        model = Cargo
        fields = ('id','cargoCod','cargoDescripcion','area')