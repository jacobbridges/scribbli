from pydash import has, get

from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.views.generic.base import View

from siteapi.models import Destination, World
from siteapi.utils import ensure_request_dict_has_one, make_error


class DestinationList(View):

    def get(self, request: HttpRequest, **kwargs):

        # Ensure the request has all the necessary data
        h = ensure_request_dict_has_one(request.GET, 'world_pk', 'world_slug')
        if h is not None:
            return h

        # Get the world object (if it exists)
        try:
            if has(request.GET, 'world_pk'):
                world = World.objects.get(pk=get(request.GET, 'world_pk'))
            else:
                world = World.objects.get(slug=get(request.GET, 'world_slug'))
        except World.DoesNotExist:
            return JsonResponse(make_error('This world does not exist.'),
                                status=404)

        # Get destinations for the current world
        # TODO: Filter destinations on writer's permissions
        destinations = Destination.objects.filter(world=world)

        # Serialize the destinations and return them
        return JsonResponse(dict(
            id='success',
            data=[d.to_dict() for d in destinations],
        ))
