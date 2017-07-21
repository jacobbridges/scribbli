import arrow

from siteapi.models import World

from django.http import JsonResponse
from django.db.models import Q
from django.views import View


class UniverseView(View):

    def get(self, request):

        # Get all worlds that this writer is allowed to see
        worlds = World.objects.filter(Q(is_public__exact=False) | Q(owner_id=request.user.id))

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
