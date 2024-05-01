from django.db import models


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    seats = models.IntegerField()
    year = models.IntegerField()
    volume = models.FloatField()