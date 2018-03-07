# -*- coding: utf-8 -*-
import logging
import json
from common import create_app_id
from beacon_conf import return_code
from beacon_app.models import *
from required_rpc import required_rpc
from django.http import JsonResponse
from beacon_rpc.forms import *

logger = logging.getLogger('rpc')


@required_rpc
def rpc_app_list(request):
    '''
    接口方法
    :param request:
    :return:
    '''
    try:
        params = json.loads(request.body)

        # 验证form
        form = AppListForm(params)
        if not form.is_valid():
            return error()
        else:
            data = request['data']
            print create_app_id()
            app_list = list(AppList.objects.all().values())
            return ok(app_list)
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
