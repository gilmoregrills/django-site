from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^gallery/$', views.media_list, name='media_list'),
    url(r'^gallery/media/(?P<pk>[0-9]+)/$', views.media_detail, name='media_detail'),
    url(r'^gallery/media/new/$', views.media_new, name='media_new'),
    url(r'^gallery/media/(?P<pk>[0-9]+)/edit/$', views.media_edit, name='media_edit'),
]