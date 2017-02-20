from django.db import models


class Signup(models.Model):
    email = models.CharField(max_length=200)
    country = models.CharField(max_length=40)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    sent_invite = models.BooleanField('sent invite', default=False)
    ip_address = models.CharField('ip address', max_length=40)
    date_created = models.DateTimeField('date created', auto_now_add=True)
