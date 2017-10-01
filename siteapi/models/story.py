from django.db import models
from django.urls.base import reverse

from siteapi.mixins.models import DateCreatedMixin, DateModifiedMixin, OwnerMixin, Serializable
from .character import Character
from .story_tag import StoryTag
from .story_status import StoryStatus


class Story(DateCreatedMixin, DateModifiedMixin, OwnerMixin):
    name = models.CharField(max_length=50, unique=True)
    slug = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    characters = models.ManyToManyField(Character, related_name='stories')
    tags = models.ManyToManyField(StoryTag, related_name='stories')
    is_public = models.BooleanField()
    status = models.ForeignKey(StoryStatus, on_delete=models.SET_NULL, related_query_name='stories',
                               null=True)

    sluggable_field = 'name'
    editable_fields = ['name', 'description', 'is_public', 'status']

    class Meta:
        unique_together = ('name', 'owner')

    def get_absolute_url(self):
        return reverse('story_detail', kwargs={'pk': self.pk})

    def serialize(self):
        data = super(Story, self).serialize()
        data.update({
            'pk': self.pk,
            'name': self.name,
            'slug': self.slug,
            'description': self.description,
            'character_pks': list(self.characters.all().values_list('pk', flat=True)),
            'tags': list(self.tags.all().values_list('slug', flat=True)),
            'is_public': self.is_public,
            'status': self.status.name,
            'status_pk': self.status.pk,
        })
        return data


class StoryMixin(models.Model, Serializable):
    story = models.ForeignKey(Story, on_delete=models.CASCADE, related_name='%(class)ss')

    class Meta:
        abstract = True

    def serialize(self):
        data = super(StoryMixin, self).serialize()
        data.update({
            'story': self.story.name,
            'story_pk': self.story.pk,
            'story_url': self.story.get_absolute_url(),
        })
        return data
