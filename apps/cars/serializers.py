from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.ModelSerializer): # ModelSerializer чіпляє дані з вже прописаної моделі, тобто не потребує прописування всіх полів
    class Meta:
        model = CarModel # модель унаслідує вже існуючу CarModel
        fields = ('id', 'brand', 'price', 'year', 'created_at', 'updated_at')
        # fields відповідає за поля, які серіалізуємо, __all__ не прописуємо, записуємо поля котрежем ('fvf', 'fvfvf', 'fffc')
