from rest_framework import serializers

from .models import AutoParkModel
from ..cars.serializers import CarSerializer


class AutoParkSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True) # вказуємо для того щоб вивело які є машини

    class Meta:
        model = AutoParkModel
        fields = ('id', 'name', 'cars')
