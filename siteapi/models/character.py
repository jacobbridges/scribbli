from django.db import models
from django.urls.base import reverse

from siteapi.mixins.models import DateCreatedMixin, DateModifiedMixin, OwnerMixin
from .image import AvatarMixin
from .race import RaceMixin
from .world import WorldMixin


class Character(DateCreatedMixin, DateModifiedMixin, OwnerMixin, WorldMixin, RaceMixin,
                AvatarMixin):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=40)
    nick = models.CharField(max_length=20, null=True, blank=True)
    description = models.TextField()

    sluggable_field = 'name'
    editable_fields = ['name', 'nick', 'description', 'world', 'race', 'avatar']

    class Meta:
        unique_together = ('name', 'owner')

    def get_absolute_url(self):
        return reverse('character_detail', kwargs={'pk': self.pk})

    def serialize(self):
        data = super(Character, self).serialize()
        data.update({
            'pk': self.pk,
            'name': self.name,
            'slug': self.slug,
            'nick': self.nick,
            'description': self.description,
        })
        return data
