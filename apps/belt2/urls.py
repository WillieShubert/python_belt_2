from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^pokeboard$', views.pokeboard),
    url(r'^poke/(?P<id>\d+)$', views.poke),
]
