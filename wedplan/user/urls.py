from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', UserList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', UserDet.as_view()),
]
