from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', SubTareaList.as_view()),
]
