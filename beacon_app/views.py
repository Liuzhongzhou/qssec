#  -*- coding:utf-8 -*-

# Create your views here.
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
    if params['name']:  # 应用系统名称
        app_query_set = app_query_set.filter(username__icontains=params['name'])

    # ip地址
    if params['ip']:  # 应用系统ip
        app_query_set = app_query_set.filter(username__icontains=params['ip'])
    # 城市
    if params['city_id']:  # 城市
        app_query_set = app_query_set.filter(username__icontains=params['city_id'])

    # 数据查询字段
    sql_keys = ['code', 'name', 'ip', 'city_id', 'add_time']
    # 返回前端字段
    show_keys = ['code', 'name', 'ip', 'city_id', 'add_time']
    # 获取分页数据
    results = common.get_paginate_data(params, app_query_set, sql_keys, show_keys)

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

    code = params.get('code', '')  # 编号

    data = dict()
    if code:
        # 数据查询字段
        sql_keys = ['code', 'name', 'ip', 'city_id', 'add_time']
        show_keys = ['code', 'name', 'ip', 'city_id', 'add_time']
        # 执行查询
        user_set = App.objects.filter(code=code)
        data = common.transform_array_column(list(user_set.values(*sql_keys)),sql_keys,show_keys)[0]

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

    code = params.get('code', '')
    name = params.get('name', '')
    ip = params.get('ip', '')
    city_id = params.get('city_id', '')

    # 修改
    if code:
        beacon_app = App.objects.filter(code=code)
        # 记录不存在
        if not beacon_app:
            return return_code.RETURN_ERROR
        # 执行更新
        beacon_app.update(name=name, ip=ip, city_id=city_id)

    # 新增
    else:
        # 执行新增
        beacon_app = App(code=uuid.uuid1(), name=name, ip=ip, city_id=city_id)
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

    code = params.get('code', '')  # 编号
    if code:

        # 执行删除
        App.objects.filter(code=code).delete()

    # 返回前端数据
    return_data = dict()
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data