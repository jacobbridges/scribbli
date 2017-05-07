from django.db import models

from .writer import Writer
from .world import World


class Race(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=40)
    description = models.TextField()
    owner = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='races',
                              related_query_name='race')
    world = models.ForeignKey(World, on_delete=models.SET_NULL, related_name='races',
                              related_query_name='race', null=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)

    class Meta:
        unique_together = ('name', 'world', 'slug')
