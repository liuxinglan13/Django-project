from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.image_create, name='create'),
    url(r'^$', views.image_list, name='list'),
]
