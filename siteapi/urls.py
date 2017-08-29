from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from siteapi.views import Signup, AlphaInvitation, Writer, Login, DestinationList
from siteapi.views.universe import UniverseDetail, UniverseList, UniverseCreate, UniverseUpdate, \
    UniverseDelete
from siteapi.views.world import WorldDetail, WorldList, WorldCreate, WorldUpdate, WorldDelete
from siteapi.views.image import ImageDetail, ImageList, ImageCreate, ImageUpdate, ImageDelete

urlpatterns = [
    url(r'^signup/', Signup.as_view(), name='signup'),
    url(r'^invitation/'
        r'(?P<unik>[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})',
        AlphaInvitation.as_view()),
    url(r'^writer/', Writer.as_view()),
    url(r'^login/', Login.as_view()),

    # Universe
    url(r'^universes/$', UniverseList.as_view(), name='universe_list'),
    url(r'^universe/$', UniverseDetail.as_view(), kwargs=dict(slug='scribbli')),
    url(r'^universe/(?P<pk>\d+)/$', UniverseDetail.as_view(), name='universe_detail'),
    url(r'^universe/create/$', UniverseCreate.as_view(), name='universe_create'),
    url(r'^universe/(?P<pk>\d+)/update/$', UniverseUpdate.as_view(), name='universe_update'),
    url(r'^universe/(?P<pk>\d+)/delete/$', UniverseDelete.as_view(), name='universe_delete'),

    # Images
    url(r'^images/$', ImageList.as_view(), name='image_list'),
    url(r'^image/(?P<pk>\d+)/$', ImageDetail.as_view(), name='image_detail'),
    url(r'^image/upload/$', ImageCreate.as_view(), name='image_create'),
    url(r'^image/upload-background/$', ImageCreate.as_view(), kwargs={'type': 'background'}, name='image_create'),
    url(r'^image/upload-avatar/$', ImageCreate.as_view(), kwargs={'type': 'avatar'}, name='image_create'),
    url(r'^image/(?P<pk>\d+)/update/$', ImageUpdate.as_view(), name='image_update'),
    url(r'^image/(?P<pk>\d+)/delete/$', ImageDelete.as_view(), name='image_delete'),

    # World
    url(r'^universe/(?P<universe_pk>\d+)/worlds/$', WorldList.as_view(), name='universe_world_list'),
    url(r'^worlds/$', WorldList.as_view(), name='world_list'),
    url(r'^world/(?P<pk>\d+)/$', WorldDetail.as_view(), name='world_detail'),
    url(r'^universe/(?P<universe_pk>\d+)/world/create/$', WorldCreate.as_view(), name='universe_world_create'),
    url(r'^world/create/$', WorldCreate.as_view(), name='world_create'),
    url(r'^world/(?P<pk>\d+)/update/$', WorldUpdate.as_view(), name='world_update'),
    url(r'^world/(?P<pk>\d+)/delete/$', WorldDelete.as_view(), name='world_delete'),

    # Destination URLs
    url(r'^destination/list/', DestinationList.as_view()),
]
