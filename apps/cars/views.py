from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404 # використовуємо замість try exception

from apps.cars.serializers import CarSerializer
from apps.cars.models import CarModel


class CarListView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)

        serializer.is_valid(raise_exception=True) # робить перевірку на вілідність, якщо перевірку не проходить то кидає помилку 'raise exeption'
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        serializer = CarSerializer(cars, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarRetrieveUpdateDestroyView(APIView):

    def get(self, *args, **kwargs):
        pk = self.kwargs['pk']
        car = get_object_or_404(CarModel, pk=pk) # витягає машину по id, якщо такої немає в наявності то інтерпретує відповідь not found
        serializer = CarSerializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = self.kwargs['pk']
        car = get_object_or_404(CarModel, pk=pk)
        data = self.request.data
        serializer = CarSerializer(car, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = self.kwargs['pk']
        car = get_object_or_404(CarModel, pk=pk)
        data = self.request.data
        serializer = CarSerializer(car, data=data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = self.kwargs['pk']
        get_object_or_404(CarModel, pk=pk).delete()
        return Response('No content',status=status.HTTP_204_NO_CONTENT)

