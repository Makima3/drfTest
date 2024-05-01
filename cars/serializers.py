from rest_framework import serializers

from .models import CarModel


class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=20)
    type = serializers.CharField(max_length=20)
    seats = serializers.IntegerField()
    year = serializers.IntegerField()
    volume = serializers.FloatField()

    def create(self, validated_data):
        car = CarModel.objects.create(**validated_data)
        return car

    def update(self, instance, validated_data:dict):
# оновлювати об'єкт можемо також за допомогою serializers#
# instance дані які оновлюємо
# validated_data вже провалідовані дані
        for k, v in validated_data.items(): #віддає кортеж ключ-значення
            setattr(instance, k, v)
            instance.save()
            return instance
# setattr дозволяє в екземпляр класу записувати значення
# instance екземпляр класу в який будемо змінювати запис, потім вказуємо по якому key і яке value
# insеance потфм зберігаємо в базу даних та повертаємо його return

class CarSerializerPartial(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    brand = serializers.CharField(max_length=20)
    year = serializers.IntegerField()
