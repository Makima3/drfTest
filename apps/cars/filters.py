from django.http import QueryDict
from django.db.models import QuerySet
from rest_framework.exceptions import ValidationError

from .models import CarModel


def car_filter(query : QueryDict) -> QuerySet:
    qs = CarModel.objects.all()
    for k, v in query.items():
        match k:
            case 'price_gt':
                qs = qs.filter(price__gt=v)
            case 'price_lt':
                qs = qs.filter(price__lt=v)
            case 'brand_end':
                qs = qs.filter(brand__iendswith=v)
            case _:
                raise ValidationError(f"'{k}' is not valid")
    return qs

