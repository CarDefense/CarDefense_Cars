from .serializers import CarSerializer
from rest_framework.viewsets import ModelViewSet
from .models import Car
# import requests


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
            token = self.request.query_params.get("token")
            return Car.objects.filter(id_token=token)

# @api_view(["POST"])
# def get_cars(request):

#     notification_token = request.data['notification_token']

#     cars = []
#     for t in Car.objects.filter(notification_token=notification_token):
#         cars.append(t.plate)

#     return Response(cars)
