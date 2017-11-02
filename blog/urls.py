#blog/urls.py

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^hello/$', views.hello, name='hello'),
    url(r'^content/(?P<pk>[0-9]+)/$', views.content, name='content'),
    url(r'^about/$', views.aboutMe, name='aboutme'),
    url(r'^contact/$', views.contact, name='contact'),
]