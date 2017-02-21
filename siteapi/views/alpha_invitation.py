import json

from django.core.serializers import serialize
from django.http import JsonResponse
from django.views import View

from siteapi.models import AlphaInvitation


class AlphaInvitationView(View):

    def get(self, request, unik):
        if not unik:
            return JsonResponse(dict(
                id='failure',
                data=dict(message='Unik cannot be empty.')
            ))
        try:
            invitation = AlphaInvitation.objects.get(unik=unik)
        except AlphaInvitation.DoesNotExist:
            return JsonResponse(dict(
                id='failure',
                data=dict(message='Could not find invitation for "{}"'.format(unik))
            ))
        return JsonResponse(dict(
            id='success',
            data=json.loads(serialize('json', [invitation],
                                      fields=('email', 'date_expires', 'accepted', 'unik')))
        ))
