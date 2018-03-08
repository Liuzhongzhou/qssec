# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
import logging
import json
from forms import *
from beacon_conf import return_code, mongodb
from models import *
import common

from django.http import JsonResponse
import bson.binary
from pymongo import MongoClient
from cStringIO import StringIO

logger = logging.getLogger('beacon_event')

def event_list(request):
    """
    事件列表
    :param request:
    :return:
    """
    params = json.loads(request.body)

    # 验证form
    form = EventListForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    event_query_set = Event.objects.all()
    # 查询条件
    if params['event_name']:  # 用户名称
        event_query_set = event_query_set.filter(username__icontains=params['event_name'])

    # 数据查询字段
    sql_keys = ['event_code', 'event_name','type','time','urgent_level','source_ip','source_port','target_ip','target_port','danger_level','status','user_name']
    # 返回前端字段
    show_keys = ['event_code', 'event_name', 'type','time','urgent_level','source_ip','source_port','target_ip','target_port','danger_level','status','user_name']

    # 获取分页数据
    results = common.get_paginate_data(params, event_query_set, sql_keys, show_keys)

    # 返回前端数据
    return_data = dict()
    return_data['data'] = results
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data

def event_info(request):
    '''
    查询事件信息
    :param request:
    :return:
    '''
    params = json.loads(request.body)

    # 验证form
    form = EventInfoForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    eventCode = params.get('event_code', '')  # 编号

    data = dict()
    if eventCode:
        # 数据查询字段
        sql_keys = ['event_code', 'event_name', 'type','time','urgent_level','source_ip','source_port','target_ip','target_port','danger_level','comment','status','user_name']
        show_keys = ['event_code', 'event_name', 'type', 'time', 'urgent_level', 'source_ip', 'source_port', 'target_ip','target_port','danger_level','comment','status','user_name']
        # 执行查询
        event_set = Event.objects.filter(event_code=eventCode)
        data['event'] = common.transform_array_column(list(event_set.values(*sql_keys)),sql_keys,show_keys)[0]
    # 返回前端数据
    return_data = dict()
    return_data["data"] = data
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data

def event_save(request):
    '''
    事件新增/修改
    :param request:
    :return:
    '''
    params = json.loads(request.body)

    # 验证form
    form = EventEditForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR
    event_code = params.get('event_code', '')  # 唯一编码
    event_name = params.get('event_name', '')  # 事件名称
    type = params.get('type', '')  # 事件类型 1-确凿类事件 2-疑似类事件 3-隐患/风险类事件'
    time = params.get('time', '')  # 发生时间
    urgent_level = params.get('urgent_level', '')  # 紧急程度
    source_ip = params.get('source_ip', '')  # 源ip
    source_port = params.get('source_port', '')  # 源端口
    target_ip = params.get('target_ip', '')  # 目的ip
    target_port= params.get('target_port', '')  # 目的端口
    danger_level=params.get('danger_level', '')  # 严重等级
    comment = params.get('comment', '')  # 备注
    status = params.get('status', '')  # 事件状态 0-未签收 1-签收办理中 2-下发办理中 3-上报办理中 4-已办结
    #file = params.get('file', '')  # 附件
    user_name = params.get('user_name', '')  # 用户

    # 修改
    if event_code:
        beacon_event = Event.objects.filter(event_code=event_code)
        # 记录不存在
        if not beacon_event:
            return return_code.RETURN_ERROR
        else:
            # 执行更新
            beacon_event.update(event_name=event_name, type=type,time=time,urgent_level=urgent_level,source_ip=source_ip,source_port=source_port,target_ip=target_ip,target_port=target_port,
                                danger_level=danger_level,comment=comment,status=status,user_name=user_name)

    # 新增
    else:
        code = uuid.uuid1()
        beacon_event = Event(event_code=code,event_name=event_name, type=type,time=time,urgent_level=urgent_level,source_ip=source_ip,source_port=source_port,target_ip=target_ip,target_port=target_port,
                                danger_level=danger_level,comment=comment,status=status,user_name=user_name)
        beacon_event.save()

    # 返回前端数据
    return_data = dict()
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data

def event_delete(request):
    """
    删除事件
    :param request:
    :return:
    """
    params = json.loads(request.body)

    # 验证form
    form = EventDeleteForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    ids = params.get('ids', '')  # 编号
    # 需删除id数组
    id_list = ids.split(',')

    if id_list:
        # 执行删除
        Event.objects.filter(event_code__in=id_list).delete()

    # 返回前端数据
    return_data = dict()
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data

def event_flow_list(request):
    """
    事件流转列表
    :param request:
    :return:
    """
    params = json.loads(request.body)

    # 验证form
    form = EventFlowListForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    eventFlow_query_set = EventFlow.objects.all()
    # 查询条件
    if params['flow_user_name']:  # 用户名称
        eventFlow_query_set = eventFlow_query_set.filter(flow_user_name__icontains=params['flow_user_name'])

    # 数据查询字段
    sql_keys = ['flow_id', 'event_code','flow_type','flow_comment','flow_user_name','flow_app__name','flow_examine','flow_result','flow_status']
    # 返回前端字段
    show_keys = ['flow_id', 'event_code', 'flow_type','flow_comment','flow_user_name','flow_app_name','flow_examine','flow_result','flow_status']

    # 获取分页数据
    results = common.get_paginate_data(params, eventFlow_query_set, sql_keys, show_keys)

    # 返回前端数据
    return_data = dict()
    return_data['data'] = results
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data

def event_flow_info(request):
    '''
    查询事件流转信息
    :param request:
    :return:
    '''
    params = json.loads(request.body)

    # 验证form
    form = EventFlowInfoForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    flow_id = params.get('flow_id', '')  # 编号

    data = dict()
    if flow_id:
        # 数据查询字段
        sql_keys = ['flow_id', 'event_code', 'flow_type', 'flow_comment', 'flow_user_name', 'flow_app__name',
                    'flow_examine', 'flow_result', 'flow_status']
        show_keys = ['flow_id', 'event_code', 'flow_type', 'flow_comment', 'flow_user_name', 'flow_app_name', 'flow_examine',
                     'flow_result', 'flow_status']
        # 执行查询
        event_flow_set = EventFlow.objects.filter(flow_id=flow_id)
        data['event_flow'] = common.transform_array_column(list(event_flow_set.values(*sql_keys)),sql_keys,show_keys)[0]
    # 返回前端数据
    return_data = dict()
    return_data["data"] = data
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data

def event_flow_save(request):
    '''
    事件流转 新增/修改
    :param request:
    :return:
    '''
    params = json.loads(request.body)

    # 验证form
    form = EventFlowEditForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR
    flow_id = params.get('flow_id', '')  # 唯一编码
    event_code = params.get('event_code', '')  # 事件编码
    flow_type = params.get('flow_type', '')  # 流转类型 1-下发 2-上报
    flow_comment = params.get('flow_comment', '')  # 流转备注
    flow_user_name = params.get('flow_user_name', '')  # 用户名
    flow_app_id = params.get('flow_app_id', '')  # 关联app
    flow_examine = params.get('flow_examine', '')  # 是否需要审核 0-不需要 1-需要
    flow_result = params.get('flow_result', '')  # 反馈结果
    flow_status = params.get('flow_status', '')  # 流转状态 0-未签收 1-签收办理中 2-已办结 4-上报至其他应用于系统系统 5-下发至其他应用系统

    # 修改
    if flow_id:
        beacon_eventFlow = EventFlow.objects.filter(flow_id=flow_id)
        # 记录不存在
        if not beacon_eventFlow:
            return return_code.RETURN_ERROR
        else:
            app = App.objects.get(code=flow_app_id)
            # 执行更新
            beacon_eventFlow.update(event_code=event_code, flow_type=flow_type,flow_comment=flow_comment,flow_user_name=flow_user_name,flow_app=app,flow_examine=flow_examine,flow_result=flow_result,flow_status=flow_status)

    # 新增
    else:
        id = uuid.uuid1()
        app = App.objects.get(code=flow_app_id)
        beacon_eventFlow = EventFlow(flow_id=id,event_code=event_code, flow_type=flow_type,flow_comment=flow_comment,flow_user_name=flow_user_name,flow_app=app,flow_examine=flow_examine,flow_result=flow_result,flow_status=flow_status)
        beacon_eventFlow.save()

    # 返回前端数据
    return_data = dict()
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def upload_file(request):
    client = MongoClient(mongodb.MongodbInfo['ip'], mongodb.MongodbInfo['port'])
    # 获得一个database
    db = client.MongoFile
    # 获得一个collection
    coll = db.image
    # 获取文件对象
    file = request.FILES.get("file", None)
    # 获取文件名称
    filename = str(request.FILES['file'])
    content = StringIO(file.read())
    # 保存
    coll.save(dict(
        content=bson.binary.Binary(content.getvalue()),
        filename=filename,
        id=uuid.uuid1()
    ))
    # 返回前端数据
    return_data = dict()
    return_data.update(return_code.RETURN_SUCCESS)
    return JsonResponse(return_data, safe=False)


# def getFile():
#     client = MongoClient('192.168.12.37', 27017)
#     # 获得一个database
#     db = client.MongoFile
#     # 获得一个collection
#     coll = db.image
#     data = coll.find_one({'filename': 'titanic_train.sql'})
#     out = open('/Users/xiong/Desktop/777.txt'.decode('utf-8'), 'wb')
#     out.write(data['content'])
#     out.close()
#     print "读取成功！！！"