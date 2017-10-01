from django.db import models
from django.urls.base import reverse

from siteapi.mixins.models import DateModifiedMixin, DateCreatedMixin, OwnerMixin, Serializable
from .story import StoryMixin
from .destination import DestinationMixin


class Chapter(DateCreatedMixin, DateModifiedMixin, OwnerMixin, StoryMixin, DestinationMixin):
    name = models.CharField(max_length=40)
    slug = models.CharField(max_length=40)
    description = models.TextField()
    is_open = models.BooleanField(default=True)

    sluggable_field = 'name'
    editable_fields = ['name', 'description', 'destination', 'story', 'is_open']

    class Meta:
        unique_together = ('name', 'story')

    def get_absolute_url(self):
        return reverse('chapter_detail', kwargs={'pk': self.pk})

    def serialize(self):
        data = super(Chapter, self).serialize()
        data.update({
            'pk': self.pk,
            'name': self.name,
            'slug': self.slug,
            'description': self.description,
            'is_open': self.is_open,
        })
        return data


class ChapterMixin(models.Model, Serializable):
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='%(class)ss')

    class Meta:
        abstract = True

    def serialize(self):
        data = super(ChapterMixin, self).serialize()
        data.update({
            'chapter': self.chapter.name,
            'chapter_pk': self.chapter.pk,
            'chapter_url': self.chapter.get_absolute_url(),
        })
        return data
