from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^dashboard$', views.dashboard),
    url(r'^users/(?P<id>\d+)/$', views.user_info),
    url(r'^favorites/(?P<id>\d+)/$', views.favorites),
    url(r'^remove/(?P<id>\d+)/$', views.remove),
    url(r'^add_quote$', views.add_quote),
]