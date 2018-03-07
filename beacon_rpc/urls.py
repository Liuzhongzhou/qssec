#  -*- coding:utf-8 -*-

from django.conf.urls import  url
import views

urlpatterns = [
    url(r'^app_list/$', views.rpc_app_list, name="app_list"),
]
