from django.db import models

from siteapi.mixins.models import DateCreatedMixin, DateModifiedMixin, IconMixin, Serializable


class StoryTag(DateCreatedMixin, DateModifiedMixin, IconMixin):
    name = models.CharField(max_length=20, unique=True)
    slug = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    sluggable_field = 'name'
    editable_fields = ['name', 'description']

    def serialize(self):
        data = super(StoryTag, self).serialize()
        data.update({
            'pk': self.pk,
            'name': self.name,
            'slug': self.slug,
            'description': self.description,
        })
        return data


class StoryTagMixin(models.Model, Serializable):
    tags = models.ManyToManyField(StoryTag, related_name='%(class)ss')

    class Meta:
        abstract = True

    def serialize(self):
        data = super(StoryTagMixin, self).serialize()
        tags = self.tags.all()
        tag_dicts = map(lambda t: dict(
            tag_pk=t.pk,
            tag_name=t.name,
            tag_slug=t.slug,
            tag_description=t.description,
        ), tags)
        data.update({
            'tags': list(tag_dicts)
        })
        return data
