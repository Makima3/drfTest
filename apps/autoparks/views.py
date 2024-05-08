from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .models import AutoParkModel
from .serializer import AutoParkModelSerializer
from apps.cars.serializer import CarModelSerializer


class AutoParkListCreateView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkModelSerializer


class AutoParkAddCarsView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    def post(self, *args, **kwargs):
        autopark = self.get_object()
        data = self.request.data
        serializer = CarModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(autopark=autopark)
        autopark_serializer = AutoParkModelSerializer(autopark)
        return Response(autopark_serializer.data, status=status.HTTP_201_CREATED)
