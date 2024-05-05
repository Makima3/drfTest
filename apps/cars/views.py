from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.cars.serializers import CarSerializer


class CarListView(APIView):
    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = CarSerializer(data=data)

        serializer.is_valid(raise_exception=True) # робить перевірку на вілідність, якщо перевірку не проходить то кидає помилку 'raise exeption'
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

