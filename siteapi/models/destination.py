from django.contrib.auth.models import User
from django.db import models

from .image import UploadedImage
from .world import World


class Destination(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=40)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='destinations',
                              related_query_name='destination')
    world = models.ForeignKey(World, on_delete=models.CASCADE, related_name='destinations',
                              related_query_name='destination')
    background = models.OneToOneField(UploadedImage, on_delete=models.CASCADE, related_name='+')
    thumbnail = models.OneToOneField(UploadedImage, on_delete=models.CASCADE, related_name='+')
    region = models.ForeignKey('Destination', on_delete=models.CASCADE, related_name='destinations',
                               related_query_name='destination')
    is_region = models.BooleanField()
    is_public = models.BooleanField()
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)

    class Meta:
        unique_together = ('name', 'world', 'slug')
