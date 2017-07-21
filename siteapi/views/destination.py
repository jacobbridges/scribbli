from django.http.request import HttpRequest
from django.http.response import JsonResponse
from django.views.generic.base import View

from siteapi.auth import authenticate_via_cookie
from siteapi.models import Destination, World
from siteapi.utils import ensure_request_dict_has_one, make_error


class DestinationList(View):

    @authenticate_via_cookie
    def get(self, request: HttpRequest, **kwargs):

        # Check that either the world's pk or slug was passed with the request
        ensure_request_dict_has_one(request.GET, ('world_pk', 'world_slug'))

        # Try to get the world
        try:
            if 'world_pk' in request.GET:
                world = World.objects.get(pk=request.GET['world_pk'])
            else:
                world = World.objects.get(slug=request.GET['world_slug'])
        except World.DoesNotExist:
            return JsonResponse(make_error('This world does not exist.'),
                                status=404)

        # Get destinations by the current writer's permissions
