# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone as timezone
from django.contrib.auth.models import AbstractUser
from django.db import models


class App(models.Model):
    '''
    app注册
    '''
    app_code = models.CharField(u'唯一编码', max_length=50, primary_key=True)
    app_name = models.CharField(u'应用系统名称', max_length=128, null=True, blank=True)
    app_ip = models.CharField(u'ip地址', max_length=50, null=True, blank=True)
    app_port = models.CharField(u'端口', max_length=50, null=True, blank=True)
    city_code = models.CharField(u'所属地市', max_length=256, null=True, blank=True)
    add_time = models.DateTimeField(u'添加日期', default=timezone.now)

    class Meta:
        db_table = 't_app'


class AppList(models.Model):
    '''
    app列表
    '''
    app_code = models.CharField(u'唯一编码', max_length=50, primary_key=True)
    app_name = models.CharField(u'应用系统名称', max_length=128, null=True, blank=True)
    app_ip = models.CharField(u'ip地址', max_length=50, null=True, blank=True)
    app_port = models.CharField(u'端口', max_length=50, null=True, blank=True)
    city_code = models.CharField(u'所属地市', max_length=256, null=True, blank=True)
    add_time = models.DateTimeField(u'添加日期', default=timezone.now)

    class Meta:
        db_table = 't_app_list'
