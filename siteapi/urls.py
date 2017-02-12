from django.conf.urls import url

import siteapi.views

urlpatterns = [
    url(r'^$', siteapi.views.signup, name='signup'),
]
