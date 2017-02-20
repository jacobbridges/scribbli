from django.conf.urls import url

import alpha.views


urlpatterns = [
    url(r'^$', alpha.views.index, name='index'),
]
