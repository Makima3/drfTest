from django.db import models

from apps.autoparks.models import AutoParkModel


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=20)
    year = models.IntegerField()
    price = models.IntegerField()
    autopark = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')