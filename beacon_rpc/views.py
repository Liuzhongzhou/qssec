# -*- coding: utf-8 -*-
import logging
import json
import base64
from common import DateEncoder
from beacon_conf import return_code
from beacon_app.models import *
from required_rpc import required_rpc
from django.http import JsonResponse
from beacon_rpc.forms import *

logger = logging.getLogger('rpc')


@required_rpc
def rpc_app_list(request):
    '''
    接口获取应用列表
    :param request:
    :return:
    '''
    try:
        params = getattr(request, request.method)
        if not params:
            params = json.loads(request.body)

        # 验证form
        form = AppListForm(params)
        if not form.is_valid():
            return error()
        else:
            data = params['data']
            if data:
                app = json.loads(base64.decodestring(data))
                app_list_obj, bool = AppList.objects.get_or_create(app_code=app['app_code'])
                if bool or app_list_obj.add_time.strftime('%Y-%m-%d %H:%M:%S') != app['add_time']:
                    app_list_obj.add_time = app['app_name']
                    app_list_obj.app_ip = app['app_ip']
                    app_list_obj.app_port = app['app_port']
                    app_list_obj.city_code = app['city_code']
                    app_list_obj.add_time = app['add_time']
                    app_list_obj.save()
            app_list = list(AppList.objects.all().values())
            return ok(data=base64.encodestring(json.dumps(list(app_list), cls=DateEncoder)))
    except Exception as e:
        logger.info(e)
        return error()


@required_rpc
def rpc_event_up(request):
    '''
    事件上报或下发
    :param request:
    :return:
    '''
    try:
        params = getattr(request, request.method)
        if not params:
            params = json.loads(request.body)

        # 验证form
        form = EventUpForm(params)
        if not form.is_valid():
            return error()
        else:
            data = params['data']
            if data:
                event_json = json.loads(base64.decodestring(data))
                print event_json

            return ok(data='ok')
    except Exception as e:
        logger.info(e)
        return error()


def ok(data):
    '''
    正确返回
    :param data:
    :return:
    '''
    return_data = dict()
    return_data['data'] = data
    return_data.update(return_code.RETURN_SUCCESS)
    return JsonResponse(return_data, safe=False)


def error():
    '''
    出错
    :return:
    '''
    return_data = dict()
    return_data.update(return_code.RETURN_ERROR)
    return JsonResponse(return_data, safe=False)
