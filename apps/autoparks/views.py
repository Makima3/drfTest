from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import AutoParkModel
from .serializers import AutoParkSerializer
from apps.cars.serializers import CarSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkSerializer


class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParkModel.objects.all() # витягаємо амвтопарк до якого по id будемо додавати машину

    def post(self, *args, **kwargs):
        autopark = self.get_object() # get_object візьме автопарк по id до якого будемо додавати машину
        data = self.request.data # інформація яку прислав user
        serializer = CarSerializer(data=data) # дані що прислав user заганяємо в серіалайзер
        serializer.is_valid(raise_exception=True) # перевіряємо чи дані валідні, якщо ні - то кидаємо помилку
        serializer.save(autopark=autopark) # якщо дані валідні то зберігаємо їх, при тому до методу save() треба додати id автопарку auto_park=auto_park -> передаючи весь об'єкт або uto_park=auto_park.id лише id
        autopark_serializer = AutoParkSerializer(autopark) # після збереження виводимо інфу про автопарк разом з машинами
        return Response(autopark_serializer.data, status=status.HTTP_201_CREATED) # віддаємо інфу з усіма автопарками та машинками

        