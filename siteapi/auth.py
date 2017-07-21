from django.http import JsonResponse
from django.http.request import HttpRequest

from scribbli.settings import COOKIE_SALT
from siteapi.token_backend import TokenBackend
from siteapi.utils import make_error, parse_token


def authenticate_via_cookie(func):

    def func_wrapper(instance, request: HttpRequest, *args, **kwargs):
        token = request.get_signed_cookie('a.t', salt=COOKIE_SALT, default=None)
        if token is None:
            return JsonResponse(make_error('Could not decode auth cookie!'))
        email, name, scopes = parse_token(token)
        try:
            writer = Writer.objects.get(email=email, token=token)
        except Writer.DoesNotExist:
            response = JsonResponse(
                make_error('Could not authenticate via cookies, try logging in.'))
            response.delete_cookie('a.t')
            return response
        kwargs['writer'] = writer
        return func(instance, request, *args, **kwargs)

    return func_wrapper
