from django.contrib.auth.models import User
from django.db import models

from siteapi.utils import one_day_from_now


class AlphaInvitation(models.Model):
    email = models.CharField(max_length=200)
    unik = models.CharField(max_length=36)
    inviter = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='invites',
                                related_query_name='invite', null=True)
    accepted = models.BooleanField(default=False)
    sent_invite = models.BooleanField('sent invite', default=False)
    date_expires = models.DateTimeField('date expires',
                                        default=one_day_from_now)
    date_created = models.DateTimeField('date created', auto_now_add=True)
    date_accepted = models.DateTimeField('date accepted', null=True)
