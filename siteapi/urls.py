from django.conf.urls import url

from siteapi.views import Signup, AlphaInvitation, Writer, Login, World

urlpatterns = [
    url(r'^signup/', Signup.as_view(), name='signup'),
    url(r'^invitation/'
        r'(?P<unik>[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})',
        AlphaInvitation.as_view()),
    url(r'^writer/', Writer.as_view()),
    url(r'^login/', Login.as_view()),
    url(r'^world/', World.as_view()),
]
