# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone as timezone
from django.db import models


class App(models.Model):
    '''
    app注册
    '''
    code = models.CharField(u'唯一编码', max_length=50, primary_key=True)
    name = models.CharField(u'应用系统名称', max_length=128)
    ip = models.CharField(u'ip地址', max_length=50)
    city_id = models.CharField(u'所属地市', max_length=256)
    add_time = models.DateTimeField(u'添加日期', default=timezone.now)

    class Meta:
        db_table = 't_app'


class AppList(models.Model):
    '''
    app列表
    '''
    code = models.CharField(u'唯一编码', max_length=50, primary_key=True)
    name = models.CharField(u'应用系统名称', max_length=128)
    ip = models.CharField(u'ip地址', max_length=50)
    city_id = models.CharField(u'所属地市', max_length=256)
    add_time = models.DateTimeField(u'添加日期', default=timezone.now)

    class Meta:
        db_table = 't_app_list'
