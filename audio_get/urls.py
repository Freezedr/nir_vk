from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.get_user_audio, name='get_user_audio'),
]