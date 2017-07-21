from slugify import slugify

from siteapi.utils import make_error, make_thumbnail
from siteapi.models import Character, Destination, Story, StoryPost, UploadedImage, World
from siteapi.forms import WorldForm

from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.views import View


class WorldView(View):

    def get(self, request):

        # Check that at least one of the required params is in the request
        if not any(['pk' in request.GET, 'slug' in request.GET]):
            return JsonResponse(make_error('Improper request: expected one of the following query '
                                           'parameters: "pk" or "slug"'))

        # Try to get the world
        try:
            world = World.objects.get(**request.GET.dict())
        except World.DoesNotExist:
            return JsonResponse(make_error('This world does not exist.'),
                                status=404)

        # Get the number of authors in this world
        destinations = Destination.objects.filter(world=world)
        num_authors = User.objects.filter(story_post__chapter__destination__in=destinations).count()

        # Serialize the world and return it
        return JsonResponse(dict(
            id='success',
            data=dict(
                name=world.name,
                slug=world.slug,
                description=world.description,
                owner=world.owner.username,
                universe=world.universe_id,
                background_path=world.background.image.url,
                thumbnail_path=world.thumbnail.image.url,
                system=world.system_id,
                is_public=world.is_public,
                date_created=world.date_created.timestamp() * 1000.0,
                date_modified=world.date_modified.timestamp() * 1000.0,
                num_characters=Character.objects.filter(world=world).count(),
                num_stories=Story.objects.filter(chapter__destination__world=world).count(),
                num_posts=StoryPost.objects.filter(chapter__destination__world=world).count(),
                num_destinations=destinations.count(),
                num_authors=num_authors,
            )
        ))

    def post(self, request):

        # Fill a form from the passed in data
        form = WorldForm(request.POST)

        # If the form fails validation, return the form errors
        if not form.is_valid():
            print(form.errors.as_data())
            return JsonResponse(make_error('Validation errors were found in request.', form.errors))

        # If the form is valid, create the world
        world = form.save(commit=False)
        world.slug = slugify(world.name)
        world.owner = request.user

        try:
            # Save the background image
            background = UploadedImage(image=request.FILES['background'], owner=request.user,
                                       type='background')
            background.save()

            # Save a thumbnail of the background
            thumbnail_file = make_thumbnail(background.image.path)
            thumbnail = UploadedImage(image=thumbnail_file, owner=request.user, type='thumbnail')
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
                owner=request.user.username,
                universe=world.universe_id,
                background_path=world.background.image.url,
                thumbnail_path=world.thumbnail.image.url,
                system=world.system_id,
                is_public=world.is_public,
                date_created=world.date_created.timestamp() * 1000.0,
                date_modified=world.date_modified.timestamp() * 1000.0,
            )
        ))
