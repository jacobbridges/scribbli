from django.contrib.auth.models import User
from django.db import models

from .story import Story
from .destination import Destination


class Chapter(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=40)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chapters',
                              related_query_name='chapter')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE,
                                    related_name='chapters', related_query_name='chapter')
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='chapters',
                              related_query_name='chapter')
    is_closed = models.BooleanField(default=False, blank=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)

    class Meta:
        unique_together = ('name', 'story', 'slug')
