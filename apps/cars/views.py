
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, CreateModelMixin
# get_object_or_404використовуємо замість try exception
# GenericAPIView розширює клас  APIView
# GenericAPIView унаслідується від APIView

from apps.cars.serializers import CarSerializer
from apps.cars.models import CarModel


# class CarListView(APIView):
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         serializer.is_valid(raise_exception=True) # робить перевірку на вілідність, якщо перевірку не проходить то кидає помилку 'raise exeption'
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def get(self, *args, **kwargs):
#         cars = CarModel.objects.all() # -> звичайний запит в БД (print(cars.query) -> записаний у текстовому варіанті SELECT, запит у БД робтить print(cars))
#         serializer = CarSerializer(cars, many=True) # -> serializer робить запит в БД і повертає об'єкти
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# class CarRetrieveUpdateDestroyView(APIView):
#
#     def get(self, *args, **kwargs):
#         pk = self.kwargs['pk']
#         car = get_object_or_404(CarModel, pk=pk) # витягає машину по id, якщо такої немає в наявності то інтерпретує відповідь not found
#         serializer = CarSerializer(car)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         pk = self.kwargs['pk']
#         car = get_object_or_404(CarModel, pk=pk)
#         data = self.request.data
#         serializer = CarSerializer(car, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         pk = self.kwargs['pk']
#         car = get_object_or_404(CarModel, pk=pk)
#         data = self.request.data
#         serializer = CarSerializer(car, data=data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         pk = self.kwargs['pk']
#         get_object_or_404(CarModel, pk=pk).delete()
#         return Response('No content',status=status.HTTP_204_NO_CONTENT)
#

class CarListView(GenericAPIView, ListModelMixin, CreateModelMixin):
    # так як клас створює та показує список, то застосовуємо відповідні mixins (при наявності GenericAPIView)
    queryset = CarModel.objects.all() # необхідний щоб витягти всі
    serializer_class = CarSerializer # конвертувати в дікт і віддати клієнту

    def get(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
# виставляємо методи відповідних mixins

    def post(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CarRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = CarModel.objects.all() # прописані queryset і serializer_class дають можливість використовувати mixins
    serializer_class = CarSerializer

    def get(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)








