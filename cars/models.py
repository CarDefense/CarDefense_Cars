from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=50, blank=True, default='')
    color = models.CharField(max_length=50, blank=True,
    default='')
    plate = models.CharField(max_length=8)
    id_token = models.IntegerField()
