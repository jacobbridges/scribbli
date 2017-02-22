import json

from passlib.hash import pbkdf2_sha256

from django.core.serializers import serialize
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from django.http import JsonResponse
from django.views import View

from siteapi.models import Writer, AlphaInvitation
from siteapi.utils import make_error, match_email_rgx, match_writer_rgx


class WriterView(View):

    required_keys = ['email', 'name', 'password']

    def post(self, request):
        """Create a writer."""
        if not request.content_type == 'application/json':
            return JsonResponse(make_error('Expected application/json'))
        data = json.loads(request.read().decode('utf8'))
        validation_errors = self.validate_post(data)
        if validation_errors:
            return JsonResponse(make_error('Data failed validation', validation_errors))
        # Check if a writer already exists for this name or email address
        try:
            writer = Writer.objects.get(name=data['name'])
            if writer:
                return JsonResponse(make_error('That pseudonym is taken.'))
            writer = Writer.objects.get(email=data['email'])
            if writer:
                return JsonResponse(make_error('This email has already been registered!'))
        except Writer.DoesNotExist:
            pass
        # Create a password hash
        phash = pbkdf2_sha256.using(salt_size=8).hash(data['password'])
        # Create the writer object
        writer = Writer(email=data['email'], name=data['name'], phash=phash)
        # Before saving the writer to the database, check if the writer was created from
        # an invitation
        unik = data.get('unik', None)
        if unik:
            invitation = AlphaInvitation.objects.get(unik=unik)
            if not invitation:
                return JsonResponse(make_error('Invitation not found for "%s"' % unik))
            if invitation.accepted:
                return JsonResponse(make_error('This invitation has already been used'))
            invitation.accepted = True
            invitation.date_accepted = now()
            invitation.save()
        try:
            writer.full_clean()
        except ValidationError as e:
            return JsonResponse(make_error('Data failed validation', e.error_list))
        writer.save()
        return JsonResponse(dict(
            id='success',
            data=json.loads(serialize('json', [writer],
                                      fields=('email', 'name', 'date_created')))
        ))

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
            # Verify that name is valid
            name = data['name']
            if type(name) is not str:
                errors.append('"name" should be a string.')
            if not match_writer_rgx(name):
                errors.append('"name" is not a valid writer\'s name.')
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
