from django.utils.timezone import now
from datetime import timedelta
from django.db import models

from .writer import Writer


def one_day_from_now():
    return now() + timedelta(days=1)


class AlphaInvitation(models.Model):
    email = models.CharField(max_length=200)
    unik = models.CharField(max_length=36)
    inviter = models.ForeignKey(Writer, on_delete=models.SET_NULL, related_name='invites',
                                related_query_name='invite', null=True)
    accepted = models.BooleanField(default=False)
    sent_invite = models.BooleanField('sent invite', default=False)
    date_expires = models.DateTimeField('date expires',
                                        default=one_day_from_now)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_accepted = models.DateTimeField('date accepted', null=True)