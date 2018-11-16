from rest_framework.serializers import ModelSerializer, ImageField
from .models import Car, Document


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'model', 'color', 'plate', 'id_token')


class DocumentSerializer(ModelSerializer):
    document = ImageField(max_length=None, use_url=True)

    class Meta:
        model = Document
        fields = '__all__'
