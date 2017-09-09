from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', EventoList.as_view()),
]
