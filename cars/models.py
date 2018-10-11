from django.db import models

class Car(models.Model):
    modelo = models.CharField(max_length=50, required=False,  allow_blank=True)
    cor = models.CharField(max_length=50, required=False,  allow_blank=True)
    placa = models.CharField(max_length=8)
    id_token = models.IntegerField()