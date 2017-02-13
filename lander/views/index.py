from django.shortcuts import render
from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def index(request):
    g = GeoIP2()
    ip = get_client_ip(request)
    try:
        request_info = g.city(ip)
    except AddressNotFoundError:
        request_info = dict()
        request_info['country'] = ''
        request_info['city'] = ''
        request_info['region'] = ''
        request_info['latitude'] = 0
        request_info['longitude'] = 0
    request_info['ip_address'] = ip
    return render(request, 'index.html', request_info)
