# from rest_framework.test import APITestCase, APIClient
# from django.apps import apps
# from django.test import TestCase
# from cars.apps import CarsConfig


# class NotificationsTests(APITestCase):

#     def testing_get_id_token_post(client):
#         client = APIClient()
#         client.post('/get_id_token/', {'plate': 'new plate'}, format='json')

#     def testing(client):
#         client = APIClient()
#         client.get('/get_id_token/')

#     def testing_validate_car_post(client):
#         client = APIClient()
#         client.post('/validate_car/', {'model': 'new', 'color': 'new2', 'plate': 'new3', 'id_token': '1'},
#                     format='json')


# class CarsConfigTest(TestCase):
#     def test_apps(self):
#         self.assertEqual(CarsConfig.name, 'cars')
#         self.assertEqual(apps.get_app_config('cars').name, 'cars')
