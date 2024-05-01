from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import CarModel
from .serializers import CarSerializer, CarSerializerPartial


class CarReadCreateView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarSerializerPartial(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)  # сконвертована в дікт дата


class CarRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']  # витягаємо id
        try:
            car = CarModel.objects.get(pk=pk) #  об'єкт який потрібно дістати
        except CarModel.DoesNotExist:
            raise Http404
        serializer = CarSerializer(car) # проганяємо його через серіалайзер
        return Response(serializer.data, status=status.HTTP_200_OK) # повертаємо дані клієнту

    def put(self, *args, **kwargs):
        pk = kwargs['pk'] # витягаємо id
        try:
            car = CarModel.objects.get(pk=pk) # об'єкт який потрібно оновити
        except CarModel.DoesNotExist:
            raise Http404
        data = self.request.data # дані які оновлюємо
        serializer = CarSerializer(car, data=data)
# викликаємо CarSerializer і оновлюємо instance, ним являється car,
# і додаємо туди data, яка являється тим чим ми будемо оновлювати car
        if not serializer.is_valid(): # вмкликаємо перевірку на serializer
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()# після перевірки зберігаємо
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            raise Http404
        data = self.request.data
        serializer = CarSerializer(car, partial=True, data=data) # додаємо параметр partial=True
        if not serializer.is_valid():
            return Response(serializer.errors)

        serializer.save()
        return Response(self.request.data, status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
            car.delete() # викликаємо метод delete
        except CarModel.DoesNotExist:
            raise Http404
        return Response("Deleted successfully", status=status.HTTP_204_NO_CONTENT)
