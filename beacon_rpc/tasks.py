# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals
from celery import task
from beacon_app.models import *
import logging
import json
import base64
from common import send_request, DateEncoder

logger = logging.getLogger("beacon_rpc")

'''
@task(bind=True, max_retries=10, default_retry_delay=1 * 60)
def test(*args, **kwargs):
    print '1111111111111111111111111111111111111111111'
    # app_list = list(AppList.objects.all().values())
    # logger.info(app_list)
    # print app_list
'''


@task(bind=True, max_retries=10, default_retry_delay=1 * 6)
def app_list(*args, **kwargs):
    try:
        app = App.objects.all().values().first()
        if not app:
            logger.info('app暂未注册')
        else:
            logger.info('[{}]同步应用数据.'.format(app['app_code']))
            data = base64.encodestring(json.dumps(app, cls=DateEncoder))
        # 向主节点发送请求
        response = send_request(data={'data': data})
        # 成功
        if response['return_code'] == 1:
            if response['data']:
                for app_obj in json.loads(base64.decodestring(response['data'])):
                    app_list_obj, bool = AppList.objects.get_or_create(app_code=app_obj['app_code'])
                    if bool or app_list_obj.add_time.strftime('%Y-%m-%d %H:%M:%S') != app_obj['add_time']:
                        app_list_obj.add_time = app_obj['app_name']
                        app_list_obj.app_ip = app_obj['app_ip']
                        app_list_obj.app_port = app_obj['app_port']
                        app_list_obj.city_code = app_obj['city_code']
                        app_list_obj.add_time = app_obj['add_time']
                        app_list_obj.save()
        else:
            logger.error(response['message'])
    except Exception as e:
        logger.error(e)
