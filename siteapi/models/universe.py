from django.db import models
from django.urls.base import reverse

from siteapi.mixins.models import DateModifiedMixin, DateCreatedMixin, Serializable


class Universe(DateCreatedMixin, DateModifiedMixin):
    name = models.CharField(max_length=40, unique=True)
    slug = models.CharField(max_length=40, unique=True)
    is_public = models.BooleanField()

    sluggable_field = 'name'
    editable_fields = ['name', 'is_public']

    def get_absolute_url(self):
        return reverse('universe_detail', kwargs={'pk': self.pk})

    def serialize(self):
        data = super(Universe, self).serialize()
        data.update(dict(
            pk=self.pk,
            name=self.name,
            slug=self.slug,
            is_public=self.is_public,
        ))
        return data


class UniverseMixin(models.Model, Serializable):
    universe = models.ForeignKey(Universe, on_delete=models.CASCADE, related_name='%(class)ss')

    class Meta:
        abstract = True

    def serialize(self):
        data = super(UniverseMixin, self).serialize()
        data.update({
            'universe': self.universe.name,
            'universe_pk': self.universe.pk,
            'universe_url': self.universe.get_absolute_url(),
        })
        return data
