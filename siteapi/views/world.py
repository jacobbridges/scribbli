import json

from slugify import slugify

from siteapi.auth import authenticate_via_cookie
from siteapi.utils import make_error, make_thumbnail
from siteapi.models import UploadedImage
from siteapi.forms import WorldForm

from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.http.request import HttpRequest
from django.views import View


class WorldView(View):

    @authenticate_via_cookie
    def post(self, request: HttpRequest, **kwargs):

        # Retrieve the writer from the kwargs (was added in the authenticate_via_cookie decorator)
        writer = kwargs['writer']

        # Fill a form from the passed in data
        form = WorldForm(request.POST)

        # If the form fails validation, return the form errors
        if not form.is_valid():
            print(form.errors.as_data())
            return JsonResponse(make_error('Validation errors were found in request.', form.errors))

        # If the form is valid, create the world
        world = form.save(commit=False)
        world.slug = slugify(world.name)
        world.owner = writer

        try:
            # Save the background image
            background = UploadedImage(image=request.FILES['background'], owner=writer,
                                       type='background')
            background.save()

            # Save a thumbnail of the background
            thumbnail_file = make_thumbnail(background.image.path)
            thumbnail = UploadedImage(image=thumbnail_file, owner=writer, type='thumbnail')
            test = thumbnail.image.url  # If the image was not create, this will cause an error
            thumbnail.save()

            # Add the images to the world
            world.background = background
            world.thumbnail = thumbnail
        except KeyError:
            return JsonResponse(make_error('World concept art is required!', extra=dict(
                background=[dict(message='Required')])))
        except Exception:
            import sys, traceback
            traceback.print_exc(file=sys.stdout)
            return JsonResponse(make_error('Check the world concept art!', extra=dict(
                background=[dict(message='Could not be parsed as an image!')])))

        # Save the world
        try:
            world.save()
        except IntegrityError as e:
            background.delete()
            thumbnail.delete()
            if 'slug' in str(e):
                return JsonResponse(make_error('Check the world name!', extra=dict(
                    name=[dict(message='A world with a similar name already exists.')])))
            else:
                raise e

        return JsonResponse(dict(
            id='success',
            data=dict(
                name=world.name,
                slug=world.slug,
                description=world.description,
                owner=writer.name,
                universe=world.universe_id,
                background_path=world.background.image.url,
                thumbnail_path=world.thumbnail.image.url,
                system=world.system_id,
                is_public=world.is_public,
                date_created=world.date_created.timestamp() * 1000.0,
                date_modified=world.date_modified.timestamp() * 1000.0,
            )
        ))
