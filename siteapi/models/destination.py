from django.db import models
from django.urls.base import reverse

from siteapi.mixins.models import DateCreatedMixin, DateModifiedMixin, OwnerMixin, Serializable
from .image import BackgroundMixin, AvatarMixin
from .world import WorldMixin


class Destination(models.Model, BackgroundMixin, AvatarMixin, WorldMixin, DateCreatedMixin,
                  DateModifiedMixin, OwnerMixin):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=40)
    description = models.TextField()
    parent = models.ForeignKey('Destination', on_delete=models.CASCADE, related_name='children',
                               related_query_name='child', null=True)
    is_public = models.BooleanField()

    sluggable_field = 'name'
    editable_fields = ['name', 'description', 'parent', 'is_public', 'background', 'avatar',
                       'world']

    class Meta:
        unique_together = ('name', 'world')

    def get_absolute_url(self):
        return reverse('destination_detail', kwargs={'pk': self.pk})

    def serialize(self):
        data = super(Destination, self).serialize()
        data.update({
            'name': self.name,
            'slug': self.slug,
            'description': self.description,
            'parent': self.parent.name if self.parent is not None else None,
            'parent_pk': self.parent.pk if self.parent is not None else None,
            'parent_url': self.parent.get_absolute_url() if self.parent is not None else None,
            'children_pks': list(self.children.all().values_list('pk', flat=True)),
            'is_public': self.is_public,
        })
        return data


class DestinationMixin(models.Model, Serializable):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE,
                                    related_name='%(class)ss')

    class Meta:
        abstract = True

    def serialize(self):
        data = super(DestinationMixin, self).serialize()
        data.update({
            'destination': self.destination.name,
            'destination_pk': self.destination.pk,
            'destination_url': self.destination.get_absolute_url(),
        })
        return data
