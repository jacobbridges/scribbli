from django.contrib.auth.models import User

from scribbli.settings import COOKIE_SALT
from siteapi.utils import parse_token


class TokenBackend(object):
    """
    Custom authentication backend for logging in via web token.
    """

    @staticmethod
    def authenticate(request):
        # Extract the token from the request's cookies
        token = request.get_signed_cookie('a.t', salt=COOKIE_SALT, default=None)
        if token is None:
            return None
        email, name, scopes = parse_token(token)

        # Try to get the writer associated with the token
        try:
            writer = User.objects.get(email=email, profile__token=token)
        except User.DoesNotExist:
            return None

        return writer

    @staticmethod
    def get_user(user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
