from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.core import serializers

from siteapi.models import Signup


@require_http_methods(['POST'])
def signup(request):
    if {'email', 'country', 'city', 'region', 'latitude', 'longitude', 'ip_address'} <= \
            set(request.POST.keys()):
        s = Signup(email=request.POST['email'], country=request.POST['country'],
                   city=request.POST['city'], region=request.POST['region'],
                   latitude=request.POST['latitude'], longitude=request.POST['longitude'],
                   ip_address=request.POST['ip_address'])
        s.save()
        return JsonResponse(dict(
            id='success',
            data=serializers.serialize('json', s)
        ))
