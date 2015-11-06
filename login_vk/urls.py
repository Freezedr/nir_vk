from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^callback/', views.getting_code, name='getting_code'),
    url(r'^authorize/', views.start_auth, name='start_auth')
]