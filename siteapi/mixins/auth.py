import abc

from django.shortcuts import redirect


class LoginRequiredMixin(object):

    def dispatch(self, request, *args, **kwargs):
        """Ensure that the user is logged in at the beginning of the request."""
        if request.user.is_authenticated:
            return super(LoginRequiredMixin, self).dispatch(request, *args, **args)
        else:
            return redirect('alpha')
