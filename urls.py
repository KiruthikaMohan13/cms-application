from django.urls import path
from django.conf.urls import url
from . views import post_create,post_detail,post_list,post_update,post_delete

#app_name = posts

urlpatterns = [
	url(r'^$',post_list,name="post_list"),
	url(r'^create/$',post_create,name="post_create"),
	url(r'^(?P<id>\d+)/$',post_detail,name="post_detail"),
	url(r'^(?P<id>\d+)/update/$',post_update,name="post_update"),
	url(r'^delete/$',post_delete,name="post_delete"),
]