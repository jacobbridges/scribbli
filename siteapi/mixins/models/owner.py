from django.contrib.auth.models import User
from django.db import models

from .serialize import Serializable


class OwnerMixin(models.Model, Serializable):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='%(class)ss')

    class Meta:
        abstract = True

    def serialize(self):
        data = super(OwnerMixin, self).serialize()
        data.update({
            'owner': self.owner.username,
            'owner_pk': self.owner.pk,
        })
        return data
