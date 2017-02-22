from django.db import models


class Writer(models.Model):
    email = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    phash = models.CharField(max_length=108, null=True)
    token = models.CharField(max_length=500, null=True, blank=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)
