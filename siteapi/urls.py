from django.conf.urls import url

import siteapi.views

urlpatterns = [
    url(r'^signup/', siteapi.views.signup, name='signup'),
]
