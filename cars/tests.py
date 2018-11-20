from rest_framework.test import APITestCase, APIClient
from django.apps import apps
from django.test import TestCase
from cars.apps import CarsConfig


class CarsTests(APITestCase):

    def testing_get_id_token_post(client):
        client = APIClient()
        client.post('/get_id_token/', {'plate': 'new plate'}, format='json')

    def testing(client):
        client = APIClient()
        client.get('/get_id_token/')

    def testing_validate_car_post(client):
        client = APIClient()
        client.post('/validate_car/', {'model': 'new', 'color': 'new2', 'plate': 'new3', 'id_token': '1',
                    'document': ''},
                    format='json')

    def testing_validate_same_car(self):
        data_1 = {'model': 'new', 'color': 'new2', 'plate': 'new3', 'id_token': '1', 'document': ''}
        data_2 = {'model': 'new', 'color': 'new2', 'plate': 'new3', 'id_token': '1', 'document': ''}

        self.client.post('/validate_car/', data=data_1)
        self.client.post('/validate_car/', data=data_2)

    def testing_right_delete_car(self):
        data = {'model': 'new', 'color': 'new2', 'plate': 'new3', 'id_token': 1, 'document': ''}
        self.client.post('/validate_car/', data=data)

        delete = {'plate': 'new3', 'id_token': 1}

        response2 = self.client.post('/delete_car/', delete)

        self.assertEqual(response2.status_code, 200)

    def testing_wrong_delete_car(self):
        data = {'model': 'new', 'color': 'new2', 'plate': 'new3', 'id_token': 1, 'document': ''}
        self.client.post('/validate_car/', data=data)

        delete = {'plate': 'new2', 'id_token': 2}

        self.client.post('/delete_car/', delete)


class CarsConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(CarsConfig.name, 'cars')
        self.assertEqual(apps.get_app_config('cars').name, 'cars')
