from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
# from rest_framework.pagination import PageNumberPagination
# у view ми можемо передавати пагінований список

from .serializers import CarModelSerializer
from .models import CarModel


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    # pagination_class = PageNumberPagination # імпортуємо та підключаємо пагінацію
    permission_classes =


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
