# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login$', views.my_login),
    url(r'^logout$', views.my_logout),

]
