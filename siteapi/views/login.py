import json

from passlib.hash import pbkdf2_sha256

from django.http import JsonResponse
from django.http.request import HttpRequest
from django.views import View

from siteapi.models import Writer
from scribbli.settings import COOKIE_SALT
from siteapi.utils import make_error, match_email_rgx, make_token, parse_token, one_day_from_now


class LoginView(View):

    required_keys = ['email', 'password']

    def post(self, request: HttpRequest):
        """Create a new authentication token."""
        if 'a.t' in request.COOKIES:
            return self.login_via_cookie(request)
        return self.login_via_data(request)

    def login_via_cookie(self, request: HttpRequest):
        token = request.get_signed_cookie('a.t', salt=COOKIE_SALT, default=None)
        if token is None:
            JsonResponse(make_error('Could not decode auth cookie!'))
        email, name, scopes = parse_token(token)
        try:
            writer = Writer.objects.get(email=email, token=token)
        except Writer.DoesNotExist:
            response = JsonResponse(
                make_error('Could not authenticate via cookies, try logging in.'))
            response.delete_cookie('a.t')
            return response
        token = make_token(writer.email, writer.name, [])
        writer.token = token
        writer.save()
        response = JsonResponse(dict(
            id='success',
            data=dict(email=writer.email, name=writer.name, scopes=[]),
        ))
        response.set_signed_cookie('a.t', token, salt=COOKIE_SALT, expires=one_day_from_now())
        return response

    def login_via_data(self, request: HttpRequest):
        if not request.content_type == 'application/json':
            return JsonResponse(make_error('Expected application/json'))
        try:
            data = json.loads(request.read().decode('utf8'))
        except json.JSONDecodeError:
            return JsonResponse(make_error('Expected application/json'))
        validation_errors = self.validate_post(data)
        if validation_errors:
            return JsonResponse(make_error('Data failed validation', validation_errors))
        # Get the writer associated with this email address
        try:
            writer = Writer.objects.get(email=data['email'])
        except Writer.DoesNotExist:
            return JsonResponse(make_error('Could not find account for "{email}"'.format(**data)))
        # Verify that the password is correct
        if not pbkdf2_sha256.verify(data['password'], writer.phash):
            return JsonResponse(make_error('Wrong password.'))
        # Create the JSON web token
        token = make_token(writer.email, writer.name, [])
        writer.token = token
        writer.save()
        response = JsonResponse(dict(
            id='success',
            data=dict(email=writer.email, name=writer.name, scopes=[]),
        ))
        response.set_signed_cookie('a.t', token, salt=COOKIE_SALT, expires=one_day_from_now())
        return response

    def validate_post(self, data):
        """Validate POST data."""
        errors = []
        if set(self.required_keys) <= set(data.keys()):
            # Verify that email is valid
            email = data['email']
            if type(email) is not str:
                errors.append('"email" should be a string.')
            if not match_email_rgx(email):
                errors.append('"email" is not a valid email address.')
            # Verify password is valid
            password = data['password']
            if type(password) is not str:
                errors.append('"password" should be a string.')
            if len(password) < 6:
                errors.append('"password" should be 6 or more characters.')
        else:
            errors.append('The following keys are required: {}.'
                          .format(', '.join(self.required_keys)))
        return errors
