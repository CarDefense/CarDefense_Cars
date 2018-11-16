from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=50, blank=True, default='')
    color = models.CharField(max_length=50, blank=True, default='')
    plate = models.CharField(max_length=8)
    id_token = models.BigIntegerField()
    document = models.CharField(null=True, blank=True, max_length=250)


class Document(models.Model):
    document = models.ImageField(null=True, blank=True)
