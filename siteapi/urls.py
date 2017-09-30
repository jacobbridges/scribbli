from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from siteapi.views import Signup, AlphaInvitation, Writer, Login
from siteapi.views.universe import UniverseDetail, UniverseList, UniverseCreate, UniverseUpdate, \
    UniverseDelete
from siteapi.views.world import WorldDetail, WorldList, WorldCreate, WorldUpdate, WorldDelete
from siteapi.views.image import ImageDetail, ImageList, ImageCreate, ImageUpdate, ImageDelete
from siteapi.views.destination import DestinationDetail, DestinationList, DestinationCreate, DestinationUpdate, \
    DestinationDelete
from siteapi.views.race import RaceDetail, RaceList, RaceCreate, RaceUpdate, RaceDelete

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

    # Image
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
    
    # Race
    url(r'^world/(?P<world_pk>\d+)/races/$', RaceList.as_view(), name='world_race_list'),
    url(r'^races/', RaceList.as_view(), name='race_list'),
    url(r'^race/(?P<pk>\d+)/$', RaceDetail.as_view(), name='race_detail'),
    url(r'^race/create/$', RaceCreate.as_view(), name='race_create'),
    url(r'^race/(?P<pk>\d+)/update/$', RaceUpdate.as_view(), name='race_update'),
    url(r'^race/(?P<pk>\d+)/delete/$', RaceDelete.as_view(), name='race_delete'),

    # Destination
    url(r'^world/(?P<world_pk>\d+)/destinations/$', DestinationList.as_view(), name='world_destination_list'),
    url(r'^destinations/', DestinationList.as_view(), name='destination_list'),
    url(r'^destination/(?P<pk>\d+)/$', DestinationDetail.as_view(), name='destination_detail'),
    url(r'^destination/create/$', DestinationCreate.as_view(), name='destination_create'),
    url(r'^destination/(?P<pk>\d+)/update/$', DestinationUpdate.as_view(), name='destination_update'),
    url(r'^destination/(?P<pk>\d+)/delete/$', DestinationDelete.as_view(), name='destination_delete'),
]
