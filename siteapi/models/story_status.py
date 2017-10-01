from django.db import models

from siteapi.mixins.models import DateCreatedMixin, DateModifiedMixin


class StoryStatus(DateCreatedMixin, DateModifiedMixin):
    name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    sluggable_field = 'name'
    editable_fields = ['name', 'description']

    def serialize(self):
        data = super(StoryStatus, self).serialize()
        data.update({
            'pk': self.pk,
            'name': self.name,
            'slug': self.slug,
            'description': self.description,
        })
        return data
