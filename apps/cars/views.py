from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .models import CarModel
from .serializer import CarModelSerializer


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
