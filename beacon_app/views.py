#  -*- coding:utf-8 -*-

from __future__ import unicode_literals
import json
from forms import *
from beacon_conf import return_code
from models import *
import common

import uuid


def appsys_list(request):
    '''
       查询应用系统列表
       :param request:
       :return:
    '''

    params = json.loads(request.body)

    # 验证form
    form = AppListForm(params)
    if not form.is_valid:
        return return_code.API_REQUEST_PARM_ERROR

    app_query_set = App.objects.all()

    # 查询条件
    if params['app_name']:  # 应用系统名称
        app_query_set = app_query_set.filter(app_name__icontains=params['app_name'])

    # ip地址
    if params['app_ip']:  # 应用系统ip
        app_query_set = app_query_set.filter(app_ip=params['app_ip'])
    # 城市
    if params['city_code']:  # 城市
        app_query_set = app_query_set.filter(city_code=params['city_code'])

    # 数据查询字段
    sql_keys = ['app_code', 'app_name', 'app_ip', 'app_port', 'city_code', 'add_time']

    # 获取分页数据
    results = common.get_paginate_data(params, app_query_set, sql_keys)

    # 返回前端数据
    return_data = dict()
    return_data['data'] = results
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def appsys_info(request):
    '''
    查询单个应用系统
    :param request:
    :return:
    '''
    params = json.loads(request.body)

    # 验证form
    form = AppListForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    app_code = params.get('app_code', '')  # 编号

    data = dict()
    if app_code:
        # 数据查询字段
        sql_keys = ['app_code', 'app_name', 'app_ip', 'app_port', 'city_code', 'add_time']
        # 执行查询
        data = App.objects.filter(app_code=app_code).values(*sql_keys).first()

    # 返回前端数据
    return_data = dict()
    return_data["data"] = data
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def appsys_save(request):
    '''
       保存修改应用系统
       :param request:
       :return:
    '''
    params = json.loads(request.body)

    # 验证form
    form = AppListForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    app_code = params.get('app_code', '')
    app_name = params.get('app_name', '')
    app_ip = params.get('app_ip', '')
    app_port = params.get('app_port', '')
    city_code = params.get('city_code', '')

    # 修改
    if app_code:
        beacon_app = App.objects.filter(app_code=app_code)
        # 记录不存在
        if not beacon_app:
            return return_code.RETURN_ERROR
        # 执行更新
        beacon_app.update(app_name=app_name, app_ip=app_ip, app_port=app_port, city_code=city_code)

    # 新增
    else:
        # 执行新增
        beacon_app = App(code=uuid.uuid1(), app_name=app_name, app_ip=app_ip, app_port=app_port, city_code=city_code)
        beacon_app.save()

    # 返回前端数据
    return_data = dict()
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def appsys_delete(request):
    '''
    删除应用系统
    :param request:
    :return:
    '''

    params = json.loads(request.body)

    # 验证form
    form = AppListForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    app_code = params.get('app_code', '')  # 编号
    if app_code:
        # 执行删除
        App.objects.filter(app_code=app_code).delete()

    # 返回前端数据
    return_data = dict()
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data
