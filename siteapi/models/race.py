from django.db import models

from siteapi.mixins.models import DateCreatedMixin, DateModifiedMixin, OwnerMixin
from .world import WorldMixin


class Race(WorldMixin, DateCreatedMixin, DateModifiedMixin, OwnerMixin):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=40)
    description = models.TextField()

    sluggable_field = 'name'
    editable_fields = ['name', 'description', 'world']

    class Meta:
        unique_together = ('name', 'world')

    @property
    def _parent(self):
        return self.world
