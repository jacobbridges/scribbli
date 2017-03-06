from django.db import models


class Universe(models.Model):
    name = models.CharField(max_length=40, unique=True)
    is_public = models.BooleanField()
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)
