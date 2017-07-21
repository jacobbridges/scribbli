from django.contrib.auth.models import User
from django.db import models

from .chapter import Chapter
from .character import Character


class StoryPost(models.Model):
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='story_posts',
                              related_query_name='story_post')
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='posts',
                                related_query_name='post')
    pov = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='posts',
                            related_query_name='post')
    characters = models.ManyToManyField(Character, related_name='in_posts',
                                        related_query_name='in_post')
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)
