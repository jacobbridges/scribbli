import re
import jwt
import json

from datetime import timedelta
from PIL import Image, ExifTags
from io import BytesIO

from django.utils.timezone import now
from django.http import JsonResponse
from django.core.files.images import ImageFile

from scribbli.settings import SECRET_KEY


# --------------------------------------------------------------------------------------------------
# File Constants

email_regex = re.compile(r'^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{'
                         r'1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{'
                         r'2,}))$')
writer_regex = re.compile(r'^([A-Za-z][0-9A-Za-z_\- ]+)$')


def match_email_rgx(email):
    return email_regex.search(email) is not None


def match_writer_rgx(writer):
    return writer_regex.search(writer) is not None


def make_error(error, extra=None):
    if extra:
        return dict(id='failure', data=dict(message=error, extra=extra))
    return dict(id='failure', data=dict(message=error))


def make_token(email, name, scopes):
    return jwt.encode({
        'email': email,
        'name': name,
        'scopes': scopes,
    }, SECRET_KEY, algorithm='HS256')


def parse_token(token):
    decoded = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
    return decoded['email'], decoded['name'], decoded['scopes']


def one_day_from_now():
    return now() + timedelta(days=1)


def ensure_json(func):

    def wrapped(instance, request, *args, **kwargs):
        if not request.content_type == 'application/json':
            return JsonResponse(make_error('Expected application/json'))
        try:
            kwargs['parsed_data'] = json.loads(request.read().decode('utf8'))
        except json.JSONDecodeError:
            return JsonResponse(make_error('Expected application/json'))
        func(instance, request, *args, **kwargs)

    return wrapped


def make_thumbnail(img_path, width=200, height=200):
    image = Image.open(img_path)
    img_ext = img_path.split('.')[-1]
    pillow_ext = {
        'png': 'PNG',
        'jpg': 'JPEG',
        'jpeg': 'JPEG',
    }.get(img_ext, None)
    if img_ext != 'png':
        for orientation in ExifTags.TAGS.keys():
            if ExifTags.TAGS[orientation] == 'Orientation':
                break
        if image._getexif() is not None:
            exif = dict(image._getexif().items())
            if exif[orientation] == 3:
                image = image.rotate(180, expand=True)
            elif exif[orientation] == 6:
                image = image.rotate(270, expand=True)
            elif exif[orientation] == 8:
                image = image.rotate(90, expand=True)
    image.thumbnail((width, height), Image.ANTIALIAS)
    in_memory_img = BytesIO()
    image.save(in_memory_img, pillow_ext, quality=90)
    return ImageFile(in_memory_img, name=('thumbnail.' + img_ext))


def ensure_request_dict_has_one(d, *items, custom_error=False):
    """
    Ensure that a request's dictionary has at least one of the requested items.
    """
    if not any([x in d for x in items]):
        if custom_error:
            return JsonResponse(make_error(custom_error))
        else:
            return JsonResponse(
                make_error('Improper request: expected one of the following '
                           'query parameters: ' + ', '.join(items)))
