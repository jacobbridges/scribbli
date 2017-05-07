from django.db import models


class StoryTag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)
