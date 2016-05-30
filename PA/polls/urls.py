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
    url(r'^$', home_list),
    url(r'^create/$', home_create),
    url(r'^(?P<id>\d+)/$',home_detail, name="detail"),
    url(r'^(?P<id>\d+)/edit/$', home_update, name="update"),
    url(r'^delete/$', home_delete,),
]
