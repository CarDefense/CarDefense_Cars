from rest_framework import status
from .models import Car
from rest_framework.test import APITestCase, APIClient, APIRequestFactory
import json


class NotificationsTests(APITestCase):

    def testing_get(client):
        client = APIClient()
        client.get('http://192.168.0.9:8003/get_id_token/')

    def testing_private(client):
        client = APIClient()
        client.post('/validate_car/', {'model': 'new', 'color': 'new2', 'plate': 'new3', 'id_token': '1'},
                    format='json')