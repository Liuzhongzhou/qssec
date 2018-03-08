#  -*- coding:utf-8 -*-

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^app_list/$', views.rpc_app_list, name="app_list"),
    url(r'^event_up/$', views.rpc_event_up, name="event_up"),
]
