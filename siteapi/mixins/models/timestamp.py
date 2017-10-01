from django.db import models

from .serialize import Serializable


class DateCreatedMixin(models.Model, Serializable):
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    @property
    def created_timestamp(self):
        if self.date_created:
            return self.date_created.timestamp()
        else:
            return None

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
        if self.date_modified:
            return self.date_modified.timestamp()
        else:
            return None

    def serialize(self):
        data = super(DateModifiedMixin, self).serialize()
        data.update(dict(date_modified=self.modified_timestamp))
        return data


class IconMixin(models.Model, Serializable):
    icon = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def serialize(self):
        data = super(IconMixin, self).serialize()
        data.update(dict(icon=self.icon))
        return data
