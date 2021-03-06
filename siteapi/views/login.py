import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.http.request import HttpRequest
from django.views import View

from scribbli.settings import COOKIE_SALT
from siteapi.utils import make_error, match_email_rgx, make_token, parse_token, one_day_from_now

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, 'dispatch')
class LoginView(View):

    required_keys = ['email', 'password']

    def post(self, request: HttpRequest):
        """Create a new authentication token."""
        if 'a.t' in request.COOKIES:
            return self.login_via_cookie(request)
        return self.login_via_data(request)

    def login_via_cookie(self, request: HttpRequest):

        # Try to get the writer associated with the token
        writer = authenticate(request=request)
        if writer is None:
            response = JsonResponse(
                make_error('Could not authenticate via cookies, try logging in.'))
            response.delete_cookie('a.t')
            return response
        login(request, writer, backend='siteapi.token_backend.TokenBackend')

        # Create a new token and save it to the user's profile
        token = make_token(writer.email, writer.username, [])
        token = token.decode('utf8')
        writer.profile.token = token
        writer.save()

        # Create the response, attach cookies, and return
        response = JsonResponse(dict(
            success=True,
            data=dict(email=writer.email, name=writer.username, scopes=[]),
        ))
        response.set_signed_cookie('a.t', token, salt=COOKIE_SALT, expires=one_day_from_now())
        return response

    def login_via_data(self, request: HttpRequest):

        # Ensure the request is sending JSON
        if not request.content_type == 'application/json':
            return JsonResponse(make_error('Expected application/json'))

        # Try to parse the request payload
        try:
            data = json.loads(request.read().decode('utf8'))
        except json.JSONDecodeError:
            return JsonResponse(make_error('Expected application/json'))

        # Validate the request payload
        validation_errors = self.validate_post(data)
        if validation_errors:
            return JsonResponse(make_error('Data failed validation', validation_errors))

        # Get the writer associated with this email address
        try:
            writer = User.objects.get(email=data['email'])
        except User.DoesNotExist:
            return JsonResponse(make_error('Could not find account for "{email}"'.format(**data)))

        # Verify that the password is correct
        writer = authenticate(username=writer.username, password=data['password'])
        if writer is None:
            return JsonResponse(make_error('Wrong password.'))
        login(request, writer)

        # Create the JSON web token
        token = make_token(writer.email, writer.username, [])
        writer.profile.token = token
        writer.save()
        response = JsonResponse(dict(
            success=True,
            data=dict(email=writer.email, name=writer.username, scopes=[]),
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
