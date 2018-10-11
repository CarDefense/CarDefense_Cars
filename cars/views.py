from .serializers import CarSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Car


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
