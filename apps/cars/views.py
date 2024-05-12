from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView

from .serializers import CarModelSerializer
from .models import CarModel


class CarListView(ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
