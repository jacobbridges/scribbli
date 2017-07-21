from django.contrib.auth.models import User
from django.db import models

from .character import Character
from .story_tag import StoryTag
from .story_status import StoryStatus


class Story(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stories',
                              related_query_name='story')
    characters = models.ManyToManyField(Character)
    tag = models.ManyToManyField(StoryTag, related_name='tags', related_query_name='tag')
    is_public = models.BooleanField()
    status = models.ForeignKey(StoryStatus, on_delete=models.SET_NULL, related_name='status',
                               related_query_name='status', null=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)
