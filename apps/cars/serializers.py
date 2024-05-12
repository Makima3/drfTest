from rest_framework import serializers
from django.core.exceptions import ValidationError

from .models import CarModel


class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'brand', 'type', 'year', 'price')

    def validate(self, attrs): # валідація на рівні серіалайзера
# після того як пройшла вілідація по моделях ми отримуємо відвалідовані атрибути,
# вивівши атрибути print(attrs), ми отрмуємо дікт з провалідованими даними
        year_ = attrs.get('year')
        price_ = attrs.get('price')
        if year_ == price_:
            raise serializers.ValidationError({'details': f'{year_=}=={price_=}'})
        return attrs

    def validate_year(self, year): # через андескор пишемо, яку ми поле хочемо конкретнно провалідувати
        if year > 1990:
            raise serializers.ValidationError({'details': f'{year=}>1990'}) # якщо виставлене значення відповідає умові то кидаємо помилку
        return year


