from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView # generic, що використовується міксинами містить уже прописанв CRUD операції
# GenericAPIView розширює клас  APIView
# GenericAPIView унаслідується від APIView

from apps.cars.serializers import CarSerializer
from apps.cars.models import CarModel


class CarListView(ListCreateAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer









