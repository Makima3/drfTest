from django.db import models
from django.core import validators as V
from datetime import datetime # для встановлення дати

from apps.autoparks.models import AutoParkModel
from .choices import CarChoices


class CarModel(models.Model):
    class Meta:
        db_table = 'cars'
    brand = models.CharField(max_length=50, validators= [V.RegexValidator('^[A-Z][a-zA-z]{2,19}$', [
        'first letter uppercase',
        'min 3',
        'max 20'
    ])])
    type = models.CharField(max_length=50, choices=[*CarChoices.choices])
    year = models.IntegerField(validators=[V.MinValueValidator(1989), V.MaxValueValidator(datetime.now().year)])
    price = models.IntegerField(validators=[V.MinValueValidator(1000), V.MaxValueValidator(1_000_000)])
    autopark = models.ForeignKey(AutoParkModel, on_delete=models.CASCADE, related_name='cars')


