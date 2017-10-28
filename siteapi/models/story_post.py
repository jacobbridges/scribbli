from django.db import models
from django.urls.base import reverse

from siteapi.mixins.models import DateCreatedMixin, DateModifiedMixin, OwnerMixin, Serializable
from .chapter import ChapterMixin
from .character import Character


class StoryPost(DateCreatedMixin, DateModifiedMixin, OwnerMixin, ChapterMixin):
    text = models.TextField()
    pov = models.ForeignKey(Character, on_delete=models.CASCADE, related_name='posts', null=True,
                            blank=True)
    characters = models.ManyToManyField(Character, related_name='in_posts')

    editable_fields = ['text', 'pov', 'chapter']

    def get_absolute_url(self):
        return reverse('story_post_detail', kwargs={'pk': self.pk})

    def serialize(self):
        data = super(StoryPost, self).serialize()
        data.update({
            'pk': self.pk,
            'text': self.text,
            'pov': self.pov.name if self.pov is not None else None,
            'pov_pk': self.pov.pk if self.pov is not None else None,
            'pov_url': self.pov.get_absolute_url() if self.pov is not None else None,
            'character_pks': list(self.characters.all().values_list('pk', flat=True)),
        })
        return data
    
    
class StoryPostMixin(models.Model, Serializable):
    story_post = models.ForeignKey(StoryPost, on_delete=models.CASCADE, related_name='%(class)ss')

    class Meta:
        abstract = True

    def serialize(self):
        data = super(StoryPostMixin, self).serialize()
        data.update({
            'story_post': self.story_post.text,
            'story_post_pk': self.story_post.pk,
            'story_post_url': self.story_post.get_absolute_url(),
        })
        return data
