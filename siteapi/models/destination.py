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
                               related_query_name='destination', null=True)
    is_region = models.BooleanField()
    is_public = models.BooleanField()
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)

    class Meta:
        unique_together = ('name', 'world', 'slug')

    def get_absolute_url(self):
        return f'/destination/?pk={self.id}'

    def to_dict(self):
        """Transform a Destination instance into a JSON safe dictionary."""
        return dict(
            name=self.name,
            slug=self.slug,
            description=self.description,
            owner=self.owner.username,
            background_path=self.background.image.url,
            thumbnail_path=self.thumbnail.image.url,
            region=None if not self.region else self.region.id,
            is_region=self.is_region,
            is_public=self.is_public,
            date_created=self.date_created.timestamp() * 1000.0,
            date_modified=self.date_modified.timestamp() * 1000.0,
            url=self.get_absolute_url(),
        )
