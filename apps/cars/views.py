from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
#from rest_framework.pagination import PageNumberPagination
from .filters import CarFilter

from .serializers import CarModelSerializer
from .models import CarModel
#from core.pagination import PagePagination


class CarListView(ListAPIView):
    serializer_class = CarModelSerializer
    #pagination_class = PagePagination
    #pagination_class = PageNumberPagination # імпортуємо з rest framework
    queryset = CarModel.objects.all()
    filterset_class = CarFilter # додаємо фільтер до view


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
