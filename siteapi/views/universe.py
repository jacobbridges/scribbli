import json
import arrow

from siteapi.auth import authenticate_via_cookie
from siteapi.models import World

from django.http.request import HttpRequest
from django.http import JsonResponse
from django.db.models import Q
from django.views import View


class UniverseView(View):

    @authenticate_via_cookie
    def get(self, request: HttpRequest, **kwargs):

        # Retrieve the writer from the kwargs (was added in the authenticate_via_cookie decorator)
        writer = kwargs['writer']

        # Get all worlds that this writer is allowed to see
        worlds = World.objects.filter(Q(is_public__exact=False) | Q(owner_id=writer.id))

        # Build the response data object
        worlds_res = []
        for world in worlds:
            worlds_res.append(dict(
                pk=world.pk,
                name=world.name,
                slug=world.slug,
                is_public=world.is_public,
                thumbnail=world.thumbnail.image.url,
                character_count=0,
                story_count=0,
                last_active=arrow.Arrow.fromdatetime(world.date_modified).humanize(),
            ))

        return JsonResponse(dict(
            id='success',
            data=worlds_res,
        ))
