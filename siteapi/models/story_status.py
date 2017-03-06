from django.db import models


class StoryStatus(models.Model):
    name = models.CharField(max_length=20, unique=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)
