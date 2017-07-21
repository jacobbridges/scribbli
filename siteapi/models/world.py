from django.contrib.auth.models import User
from django.db import models

from .image import UploadedImage
from .universe import Universe


class World(models.Model):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=40)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worlds',
                              related_query_name='world', null=True)
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE, related_name='worlds',
                                 related_query_name='world')
    background = models.OneToOneField(UploadedImage, on_delete=models.CASCADE,
                                      related_name='background')
    thumbnail = models.OneToOneField(UploadedImage, on_delete=models.CASCADE,
                                     related_name='thumbnail')
    system = models.ForeignKey('World', on_delete=models.CASCADE, related_name='children',
                               related_query_name='child', blank=True, null=True)
    is_public = models.BooleanField()
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)

    class Meta:
        unique_together = (('name', 'universe'), ('slug', 'universe'))
