from django.db import models

from core.models import BaseModel
#  з core імпортуємо модель і наступний клас, що має містити в собі певні поля, які прописані в корі наслідує BaseModel, а не Model


class CarModel(BaseModel):
        class Meta:
            db_table = 'cars'

        brand = models.CharField(max_length=20)
        price = models.IntegerField()
        year = models.IntegerField()

