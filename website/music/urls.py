from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index,  name='index'),
    url(r'^(?P<album_title>[a-z 0-9 A-Z]+)/$', views.detail, name='detail'),
    ]
