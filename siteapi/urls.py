from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from siteapi.views import Signup, AlphaInvitation, Writer, Login, World, UniverseDetail, \
    DestinationList, UniverseList, UniverseCreate, UniverseUpdate

urlpatterns = [
    url(r'^signup/', Signup.as_view(), name='signup'),
    url(r'^invitation/'
        r'(?P<unik>[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})',
        AlphaInvitation.as_view()),
    url(r'^writer/', Writer.as_view()),
    url(r'^login/', Login.as_view()),
    url(r'^world/', login_required(World.as_view())),

    # Universe
    url(r'^universes/$', UniverseList.as_view()),
    url(r'^universe/$', UniverseDetail.as_view(), kwargs=dict(slug='scribbli')),
    url(r'^universe/(?P<pk>\d+)/$', UniverseDetail.as_view()),
    url(r'^universe/create/$', UniverseCreate.as_view()),
    url(r'^universe/update/(?P<pk>\d+)/$', UniverseUpdate.as_view()),

    # Destination URLs
    url(r'^destination/list/', DestinationList.as_view()),
]
