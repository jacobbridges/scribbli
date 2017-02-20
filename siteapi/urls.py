from django.conf.urls import url

from siteapi.views import Signup, AlphaInvitation

urlpatterns = [
    url(r'^signup/', Signup.as_view(), name='signup'),
    url(r'^invitation/'
        r'(?P<unik>[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12})',
        AlphaInvitation.as_view()),
]
