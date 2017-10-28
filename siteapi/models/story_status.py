from django.db import models
from django.urls.base import reverse

from siteapi.mixins.models import DateCreatedMixin, DateModifiedMixin, Serializable


class StoryStatus(DateCreatedMixin, DateModifiedMixin):
    name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    sluggable_field = 'name'
    editable_fields = ['name', 'description']

    def get_absolute_url(self):
        return reverse('story_status_detail', kwargs={'pk': self.pk})

    def serialize(self):
        data = super(StoryStatus, self).serialize()
        data.update({
            'pk': self.pk,
            'name': self.name,
            'slug': self.slug,
            'description': self.description,
        })
        return data


class StoryStatusMixin(models.Model, Serializable):
    status = models.ForeignKey(StoryStatus, on_delete=models.CASCADE, related_name='%(class)ss')

    class Meta:
        abstract = True

    def serialize(self):
        data = super(StoryStatusMixin, self).serialize()
        data.update({
            'status': self.status.name,
            'status_description': self.status.description,
            'status_pk': self.status.pk,
            'status_url': self.status.get_absolute_url(),
        })
        return data
