from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AutoParkModelSerializer
from .models import AutoParkModel
from apps.cars.serializers import CarModelSerializer


class AutoParkListCreateAView(ListCreateAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkModelSerializer


class AutoParkRetrieveUpdateDestroyAView(RetrieveUpdateDestroyAPIView):
    queryset = AutoParkModel.objects.all()
    serializer_class = AutoParkModelSerializer


class AutoParkAddCarView(GenericAPIView):
    queryset = AutoParkModel.objects.all()

    def post(self, *args, **kwargs):
        autopark = self.get_object()
        data = self.request.data
        serializer = CarModelSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(autopark=autopark)
        ap_serializer = AutoParkModelSerializer(autopark)
        return Response(ap_serializer.data, status=status.HTTP_201_CREATED)

