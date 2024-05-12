from rest_framework import serializers

from .models import AutoParkModel
from apps.cars.serializers import CarModelSerializer


class AutoParkModelSerializer(serializers.ModelSerializer):
    cars = CarModelSerializer(many=True, read_only=True)

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'cars')
