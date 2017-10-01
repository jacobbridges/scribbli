from django.db import models

from siteapi.mixins.models import DateCreatedMixin, DateModifiedMixin, OwnerMixin, Serializable
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


class RaceMixin(models.Model, Serializable):
    race = models.ForeignKey(Race, on_delete=models.CASCADE, related_name='%(class)ss')

    class Meta:
        abstract = True

    def serialize(self):
        data = super(RaceMixin, self).serialize()
        data.update({
            'race': self.race.name,
            'race_pk': self.race.pk,
            'race_world_pk': self.race.world.pk,
        })
        return data
