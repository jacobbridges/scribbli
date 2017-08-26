from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from siteapi.views import Signup, AlphaInvitation, Writer, Login, World, Universe, DestinationList

urlpatterns = [
    url(r'^signup/', Signup.as_view(), name='signup'),
    url(r'^invitation/'
        r'(?P<unik>[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})',
        AlphaInvitation.as_view()),
    url(r'^writer/', Writer.as_view()),
    url(r'^login/', Login.as_view()),
    url(r'^world/', login_required(World.as_view())),
    url(r'^universe/', login_required(Universe.as_view())),

    # Destination URLs
    url(r'^destination/list/', DestinationList.as_view()),
]
