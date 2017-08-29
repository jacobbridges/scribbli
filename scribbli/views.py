from django.http import JsonResponse


def csrf_request(request, *args, **kwargs):
    return JsonResponse(dict(success=False, data=dict(message='Missing CSRF token.')))
