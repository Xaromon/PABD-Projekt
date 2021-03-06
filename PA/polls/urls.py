from django.conf.urls import url
from django.contrib import admin
from.views import  (
    home_list,
    home_create,
    home_detail,
    home_update,
    home_delete,

)
urlpatterns = [
    url(r'^$', home_list,name="list"),
    url(r'^create/$', home_create, name = "create"),
    url(r'^(?P<id>\d+)/$',home_detail, name="detail"),
    url(r'^(?P<id>\d+)/edit/$', home_update, name="update"),
    url(r'^(?P<id>\d+)/delete/$', home_delete,name = "delete"),
]
