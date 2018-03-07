#  -*- coding:utf-8 -*-
"""fort URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from beacon import views as beacon_views
from beacon_event.views import eveln_file

urlpatterns = [
    url(r'^admin2/', admin.site.urls),
    url(r'^api/', include('beacon_user.urls')),
    url(r'^api/$', beacon_views.home),

    # rpc请求
    url(r'^rpc/', include('beacon_rpc.urls', namespace='rpc')),

    # 文件上传
    url(r'^file/', eveln_file),
]
