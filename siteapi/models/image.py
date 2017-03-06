from uuid import uuid4

from django.db import models

from .writer import Writer


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


class UploadedImage(models.Model):
    image = models.ImageField(upload_to=generate_image_path, width_field='image_width',
                              height_field='image_height')
    image_width = models.FloatField(null=True, blank=True)
    image_height = models.FloatField(null=True, blank=True)
    type = models.CharField(max_length=40)
    owner = models.ForeignKey(Writer, on_delete=models.SET_NULL, related_name='uploaded_images',
                              related_query_name='uploaded_image', null=True)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_modified = models.DateTimeField('date modified', auto_now=True)
