from django.urls import path
from django.conf.urls import url

from posts.api.views import (
	PostListAPIView,
	PostDetailAPIView,
	PostUpdateAPIView,
	PostDeleteAPIView,)

app_name = 'posts'

urlpatterns = [
	url(r'^$',PostListAPIView.as_view(),name='list'),
	url(r'^(?P<pk>\d+)/$',PostDetailAPIView.as_view(),name='detail'),
	url(r'^(?P<pk>\d+)/update$',PostUpdateAPIView.as_view(),name='update'),
	url(r'^(?P<pk>\d+)/delete$',PostDeleteAPIView.as_view(),name='delete'),
]