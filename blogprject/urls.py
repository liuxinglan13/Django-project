"""blogprject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import notifications.urls
import xadmin


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls', namespace='blog')),
    url(r'', include('ckeditor_uploader.urls')),   #富文本编辑器ckeditor相关
    url(r'', include('easy_comment.urls')),
    url(r'^notifications/', include(notifications.urls, namespace='notifications')),
    url(r'^users/', include('users.urls')),                     # 自定义的扩展用户app
    url(r'^users/', include('django.contrib.auth.urls')),       # Django内置的用户相关操作视图
    url(r'^accounts/', include('allauth.urls')),                # django-allauth相关
    url(r'^images/', include('images.urls', namespace='images')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # 没有这一句无法显示上传的图片
