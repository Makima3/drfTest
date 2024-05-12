from django.db.models import TextChoices


class CarChoices(TextChoices): # описуємо поля які можна записувати в БД, використовуєсо лише для вичерпних списків
    Coupe = 'Coupe',
    Sedan = 'Sedan',
    SUV = 'SUV',
    Universal = 'Universal',
    Hatchback = 'Hatchback',
    Jeep = 'Jeep'
