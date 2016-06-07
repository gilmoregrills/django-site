from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^bot/$', views.message_history, name='message_history'),
]
