from django_filters import rest_framework as filters


class CarFilter(filters.FilterSet): # filters додаємо до views
    year_lt = filters.NumberFilter(field_name='year', lookup_expr='lt') # field_name вставляємо поле до якого буде застосовуватися фільтер, lookup_expr вираз за яким будемо фільтрувати lt, lte. gt,gte.
    year_gt = filters.NumberFilter(field_name='year', lookup_expr='gt')
    brand = filters.CharFilter(field_name='brand', lookup_expr='icontains')
    order = filters.OrderingFilter( # передаємо fields, по яких робимо ордеринг, кортежем
        fields=(
            '-id',
            'price',
            ('price', 'asd')# в ordering можемо змінити назву поля по якому будемо шукати перще поле по якому шукажмо, друге - псевдонім, яке вписуємо в кверю
        )
    )

