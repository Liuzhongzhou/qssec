# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery import task
from beacon_app.models import *
import logging

logger = logging.getLogger("beacon_rpc")


@task
def test(*args, **kwargs):
    print '1111111111111111111111111111111111111111111'
    # app_list = list(AppList.objects.all().values())
    # logger.info(app_list)
    # print app_list


@task
def app_list(*args, **kwargs):
    print '2222222222222222222222222222222222222222222'
    app = App.objects.all().values().first()
    if not app:
        logger.info('app暂未注册')
    else:
        logger.info('[{}]同步应用数据'.format(app['code']))
