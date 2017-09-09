from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', ComentarioList.as_view()),
]
