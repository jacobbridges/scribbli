from django.db import models

from siteapi.mixins.models import DateModifiedMixin, DateCreatedMixin


class Universe(DateCreatedMixin, DateModifiedMixin):
    name = models.CharField(max_length=40, unique=True)
    slug = models.CharField(max_length=40, unique=True)
    is_public = models.BooleanField()

    sluggable_field = 'name'
    editable_fields = ['name', 'is_public']

    def serialize(self):
        data = super(Universe, self).serialize()
        data.update(dict(
            pk=self.pk,
            name=self.name,
            slug=self.slug,
            is_public=self.is_public,
        ))
        return data
