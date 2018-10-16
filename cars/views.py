from .serializers import CarSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from .models import Car
import requests
from rest_framework.response import Response


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
            token = self.request.query_params.get("token")
            return Car.objects.filter(id_token=token)


@api_view(["POST"])
def validate_car(request):
    model = request.data['model']
    color = request.data['color']
    plate = request.data['plate']
    id_token = request.data['id_token']

    registered = False

    for t in Car.objects.filter(id_token=id_token, plate=plate):
        if(id_token == t.id_token and plate == t.plate):
            registered = True

    if(registered):
        return Response("Veículo já cadastrado para este usuário")

    else:
        task = {"model": model, "color": color, "plate": plate, "id_token": id_token}
        resp = requests.post('http://192.168.0.14:8003/car/', json=task)
        return Response(resp)


@api_view(["POST"])
def get_id_token(request):

    plate = request.data['plate']

    for t in Car.objects.filter(plate=plate):
        token = t.id_token
    
    return Response(token)
