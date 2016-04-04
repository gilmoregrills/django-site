from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^gallery/$', views.project_list, name='project_list'),
    url(r'^gallery/project/(?P<pk>[0-9]+)/$', views.project_detail, name='project_detail'),
    url(r'^gallery/project/new/$', views.project_new, name='project_new'),
    url(r'^gallery/project/(?P<pk>[0-9]+)/edit/$', views.project_edit, name='project_edit'),
]