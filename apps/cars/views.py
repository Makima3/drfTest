from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework import status
from django.db.models import Q #  використовують для позначення 'or'
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# get_object_or_404використовуємо замість try exception
# GenericAPIView розширює клас  APIView
# GenericAPIView унаслідується від APIView

from apps.cars.serializers import CarSerializer
from apps.cars.models import CarModel
from .filters import car_filter


class CarListView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params)
    # def post(self, *args, **kwargs):
    #     data = self.request.data
    #     serializer = CarSerializer(data=data)
    #     serializer.is_valid(raise_exception=True) # робить перевірку на вілідність, якщо перевірку не проходить то кидає помилку 'raise exeption'
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)
    #
    # def get(self, *args, **kwargs):
    #     # # qs = CarModel.objects.filter(price__range=(20000, 40000)).order_by('-price')
    #     # qs = CarModel.objects.all()[:2]
    #     # # виставлення лімітів ([2:4] -> перше число пропускає певну к-сть, друге - вказує які машини по рахунку взяти (3 і 4), застосовують для пагінації)
    #     # # MySQL це як ліміти і офсети
    #     # # задавати крок [2:4:2] -> третій параметр, не рекомендують робити бо це навантажує БД, і це вже не query set, а масив
    #     # qs = CarModel.objects.filter(Q(brand='Toyota') | Q(year=2015) & Q(brand='Ford') | Q(year=2018)) # or...or and or...or
    #     qs = CarModel.objects.all()
    #     serializer = CarSerializer(qs, many=True) # -> serializer робить запит в БД і повертає об'єкти
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer

    # def get(self, *args, **kwargs):
    #     pk = self.kwargs['pk']
    #     car = get_object_or_404(CarModel, pk=pk) # витягає машину по id, якщо такої немає в наявності то інтерпретує відповідь not found
    #     serializer = CarSerializer(car)
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def put(self, *args, **kwargs):
    #     pk = self.kwargs['pk']
    #     car = get_object_or_404(CarModel, pk=pk)
    #     data = self.request.data
    #     serializer = CarSerializer(car, data=data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def patch(self, *args, **kwargs):
    #     pk = self.kwargs['pk']
    #     car = get_object_or_404(CarModel, pk=pk)
    #     data = self.request.data
    #     serializer = CarSerializer(car, data=data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_200_OK)
    #
    # def delete(self, *args, **kwargs):
    #     pk = self.kwargs['pk']
    #     get_object_or_404(CarModel, pk=pk).delete()
    #     return Response('No content',status=status.HTTP_204_NO_CONTENT)








