from django.db import models
from django.urls.base import reverse

from siteapi.mixins.models import DateCreatedMixin, DateModifiedMixin, OwnerMixin, Serializable
from .image import BackgroundMixin, AvatarMixin
from .universe import UniverseMixin


class World(DateCreatedMixin, DateModifiedMixin, AvatarMixin, BackgroundMixin, OwnerMixin,
            UniverseMixin):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=40)
    description = models.TextField()
    parent = models.ForeignKey('World', on_delete=models.CASCADE, related_name='children',
                               related_query_name='child', blank=True, null=True)
    is_public = models.BooleanField()

    sluggable_field = 'name'
    editable_fields = ['name', 'description', 'parent', 'is_public', 'universe', 'background',
                       'avatar']

    class Meta:
        unique_together = ('name', 'universe')

    def get_absolute_url(self):
        return reverse('world_detail', kwargs={'pk': self.pk})

    def serialize(self):
        data = super(World, self).serialize()
        data.update({
            'pk': self.pk,
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


class WorldMixin(models.Model, Serializable):
    world = models.ForeignKey(World, on_delete=models.CASCADE, related_name='%(class)ss')

    class Meta:
        abstract = True

    def serialize(self):
        data = super(WorldMixin, self).serialize()
        data.update({
            'world': self.world.name,
            'world_pk': self.world.pk,
            'world_url': self.world.get_absolute_url(),
        })
        return data
