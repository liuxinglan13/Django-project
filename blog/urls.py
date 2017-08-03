from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetailView.as_view(), name='detail')
]