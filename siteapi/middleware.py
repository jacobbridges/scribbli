class ShortCircuitHttpChain(Exception):
    def __init__(self, *args, **kwargs):
        self.response = kwargs.get('response', None)
        super(ShortCircuitHttpChain, self).__init__('HTTP chain has been short-circuited.', *args)


class ShortCircuitMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, ShortCircuitHttpChain):
            return exception.response
        return None
