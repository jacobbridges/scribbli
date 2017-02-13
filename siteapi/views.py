import json

from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.core import serializers

from siteapi.models import Signup


@require_http_methods(['POST'])
def signup(request):
    if request.content_type == 'application/json':
        data = json.loads(request.read().decode('utf8'))
        if {'email', 'country', 'city', 'region', 'latitude', 'longitude', 'ip_address'} <= \
                set(list(data.keys())):
            s = Signup(email=data['email'], country=data['country'], city=data['city'],
                       region=data['region'], latitude=data['latitude'],
                       longitude=data['longitude'], ip_address=data['ip_address'])
            s.save()
            return JsonResponse(dict(
                id='success',
                data=serializers.serialize('json', [s])
            ))
        return JsonResponse(dict(
            id='failure',
            data=dict(message=(', '.join(['email', 'country', 'city', 'region', 'latitude',
                                          'longitude', 'ip_address']) + ' required'))
        ))
    return JsonResponse(dict(
        id='failure',
        data=dict(message='expected application/json')
    ))
