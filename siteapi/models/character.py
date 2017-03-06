from django.db import models

from .writer import Writer
from .world import World
from .race import Race


class Character(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=40)
    nick = models.CharField(max_length=20, blank=True, null=True)
    description = models.TextField()
    owner = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name='characters',
                              related_query_name='character')
    world = models.ForeignKey(World, on_delete=models.SET_NULL, related_name='characters',
                              related_query_name='character')
    race = models.ForeignKey(Race, on_delete=models.SET_NULL, related_name='characters',
                             related_query_name='character')
    is_public = models.BooleanField()
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)

    class Meta:
        unique_together = ('name', 'owner', 'slug')