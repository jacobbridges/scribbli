from django.db import models

from .serialize import Serializable


class DateCreatedMixin(models.Model, Serializable):
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    @property
    def created_timestamp(self):
        return self.date_created.timestamp()

    def serialize(self):
        data = super(DateCreatedMixin, self).serialize()
        data.update(dict(date_created=self.created_timestamp))
        return data


class DateModifiedMixin(models.Model, Serializable):
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @property
    def modified_timestamp(self):
        return self.date_modified.timestamp()

    def serialize(self):
        data = super(DateModifiedMixin, self).serialize()
        data.update(dict(date_modified=self.modified_timestamp))
        return data
