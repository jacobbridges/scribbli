from uuid import uuid4

from django.db import models

from siteapi.mixins.models import DateCreatedMixin, Serializable, OwnerMixin, \
    SerializeRelatedObjectsMixin


def generate_image_path(instance, filename):
    """
    Generates a dynamic upload path for the uploaded image.
    Image will be stored at <MEDIA_ROOT>/alpha/img/uploads/<year>/<month>/<day>/<uuid>.<ext>
    """
    return 'alpha/img/uploads/writer_{writer_id}/{type}/{hash}.{ext}'.format(
        type=instance.type,
        writer_id=instance.owner.id,
        hash=uuid4(),
        ext=filename.split('.')[-1]
    )


class UploadedImage(DateCreatedMixin, OwnerMixin, SerializeRelatedObjectsMixin):
    image = models.ImageField(upload_to=generate_image_path, width_field='image_width',
                              height_field='image_height')
    image_width = models.FloatField(null=True, blank=True)
    image_height = models.FloatField(null=True, blank=True)
    type = models.CharField(max_length=40)

    editable_fields = ['image', 'type']
    serialize_relations = True

    @property
    def name(self):
        return self.image.name.split('/')[-1]

    def serialize(self):
        data = super(UploadedImage, self).serialize()
        related_objects = []
        if self.type == 'background':
            for relation in data['related_objects']:
                if 'avatar' not in relation['relation']:
                    related_objects.append(relation)
        if self.type == 'avatar':
            for relation in data['related_objects']:
                if 'background' not in relation['relation']:
                    related_objects.append(relation)
        data['related_objects'] = related_objects
        data.update({
            'pk': self.pk,
            'name': self.name,
            'url': self.image.url,
            'width': self.image_width,
            'height': self.image_height,
            'type': self.type,
        })
        return data


class BackgroundMixin(models.Model, Serializable):
    background = models.OneToOneField(UploadedImage, on_delete=models.CASCADE,
                                      related_name='background_for_%(class)ss')

    class Meta:
        abstract = True

    @property
    def background_url(self):
        return self.background.image.url

    @property
    def background_height(self):
        return self.background.image_height

    @property
    def background_width(self):
        return self.background.image_width

    def serialize(self):
        data = super(BackgroundMixin, self).serialize()
        data.update({
            'background_pk': self.background.pk,
            'background': self.background_url,
            'background_height': self.background_height,
            'background_width': self.background_width,
        })
        return data


class AvatarMixin(models.Model, Serializable):
    avatar = models.OneToOneField(UploadedImage, on_delete=models.CASCADE,
                                  related_name='avatar_for_%(class)ss')

    class Meta:
        abstract = True

    @property
    def avatar_url(self):
        return self.avatar.image.url

    @property
    def avatar_height(self):
        return self.avatar.image_height

    @property
    def avatar_width(self):
        return self.avatar.image_width

    def serialize(self):
        data = super(AvatarMixin, self).serialize()
        data.update({
            'avatar_pk': self.avatar.pk,
            'avatar': self.avatar_url,
            'avatar_height': self.avatar_height,
            'avatar_width': self.avatar_width,
        })
        return data
