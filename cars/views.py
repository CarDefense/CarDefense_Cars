from .serializers import CarSerializer, DocumentSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from .models import Car, Document
from rest_framework.response import Response


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get_queryset(self):
        token = self.request.query_params.get("token")
        return Car.objects.filter(id_token=token)


class DocumentViewSet(ModelViewSet):
    queryset = Document.objects.filter(id=0)
    serializer_class = DocumentSerializer


@api_view(["POST"])
def validate_car(request):
    model = request.data['model']
    color = request.data['color']
    plate = request.data['plate']
    id_token = request.data['id_token']
    document = request.data['document']

    registered = False

    for car in Car.objects.filter(id_token=id_token, plate=plate):
        if(plate == car.plate):
            registered = True

    if(registered):
        return Response("Veículo já cadastrado.")

    else:
        Car.objects.create(model=model, color=color, plate=plate, id_token=id_token, document=document)
        return Response("Veículo cadastrado com sucesso.")


@api_view(["POST"])
def delete_car(request):
    plate = request.data['plate']
    id_token = request.data['id_token']

    deleted = False

    for car in Car.objects.filter(id_token=id_token, plate=plate):
        if(plate == car.plate):
            car.delete()
            deleted = True

    if (deleted):
        return Response("Veículo deletado")

    else:
        return Response("Veículo não encontrado")


@api_view(["POST"])
def get_id_token(request):

    plate = request.data['plate']
    idTokenArray = []
    for token in Car.objects.filter(plate=plate):
        idTokenArray.append(token.id_token)
    return Response(idTokenArray)
