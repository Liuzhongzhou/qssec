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
    if params['eventName']:  # 用户名称
        event_query_set = event_query_set.filter(username__icontains=params['eventName'])

    # 数据查询字段
    sql_keys = ['event_code', 'event_name','type','time','urgent_level','source_ip','source_port','target_ip','target_port','danger_level','status','user_name']
    # 返回前端字段
    show_keys = ['eventCode', 'eventName', 'type','time','urgentLevel','sourceIp','sourcePort','targetIp','targetPort','dangerLevel','status','userName']

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

    eventCode = params.get('eventCode', '')  # 编号

    data = dict()
    if eventCode:
        # 数据查询字段
        sql_keys = ['event_code', 'event_name', 'type','time','urgent_level','source_ip','source_port','target_ip','target_port','danger_level','comment','status','user_name']
        show_keys = ['eventCode', 'eventName', 'type', 'time', 'urgentLevel', 'sourceIp', 'sourcePort', 'targetIp','targetPort','dangerLevel','comment','status','userName']
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
    eventCode = params.get('eventCode', '')  # 唯一编码
    eventName = params.get('eventName', '')  # 事件名称
    type = params.get('type', '')  # 事件类型 1-确凿类事件 2-疑似类事件 3-隐患/风险类事件'
    time = params.get('time', '')  # 发生时间
    urgentLevel = params.get('urgentLevel', '')  # 紧急程度
    sourceIp = params.get('sourceIp', '')  # 源ip
    sourcePort = params.get('sourcePort', '')  # 源端口
    targetIp = params.get('targetIp', '')  # 目的ip
    targetPort= params.get('targetPort', '')  # 目的端口
    dangerLevel=params.get('dangerLevel', '')  # 严重等级
    comment = params.get('comment', '')  # 备注
    status = params.get('status', '')  # 事件状态 0-未签收 1-签收办理中 2-下发办理中 3-上报办理中 4-已办结
    #file = params.get('file', '')  # 附件
    userName = params.get('userName', '')  # 用户

    # 修改
    if eventCode:
        beacon_event = Event.objects.filter(event_code=eventCode)
        # 记录不存在
        if not beacon_event:
            return return_code.RETURN_ERROR
        else:
            # 执行更新
            beacon_event.update(event_name=eventName, type=type,time=time,urgent_level=urgentLevel,source_ip=sourceIp,source_port=sourcePort,target_ip=targetIp,target_port=targetPort,
                                danger_level=dangerLevel,comment=comment,status=status,user_name=userName)

    # 新增
    else:
        code = uuid.uuid1()
        beacon_event = Event(event_code=code,event_name=eventName, type=type,time=time,urgent_level=urgentLevel,source_ip=sourceIp,source_port=sourcePort,target_ip=targetIp,target_port=targetPort,
                                danger_level=dangerLevel,comment=comment,status=status,user_name=userName)
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

def eventFlow_list(request):
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
    if params['flowUserName']:  # 用户名称
        eventFlow_query_set = eventFlow_query_set.filter(flow_user_name__icontains=params['flowUserName'])

    # 数据查询字段
    sql_keys = ['flow_id', 'event_code','flow_type','flow_comment','flow_user_name','flow_app__name','flow_examine','flow_result','flow_status']
    # 返回前端字段
    show_keys = ['flowId', 'eventCode', 'flowType','flowComment','flowUserName','flowAppName','flowExamine','flowResult','flowStatus']

    # 获取分页数据
    results = common.get_paginate_data(params, eventFlow_query_set, sql_keys, show_keys)

    # 返回前端数据
    return_data = dict()
    return_data['data'] = results
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data

def eventFlow_info(request):
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

    flowId = params.get('flowId', '')  # 编号

    data = dict()
    if flowId:
        # 数据查询字段
        sql_keys = ['flow_id', 'event_code', 'flow_type', 'flow_comment', 'flow_user_name', 'flow_app__name',
                    'flow_examine', 'flow_result', 'flow_status']
        show_keys = ['flowId', 'eventCode', 'flowType', 'flowComment', 'flowUserName', 'flowAppName', 'flowExamine',
                     'flowResult', 'flowStatus']
        # 执行查询
        eventFlow_set = EventFlow.objects.filter(flow_id=flowId)
        data['eventFlow'] = common.transform_array_column(list(eventFlow_set.values(*sql_keys)),sql_keys,show_keys)[0]
    # 返回前端数据
    return_data = dict()
    return_data["data"] = data
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data

def eventFlow_save(request):
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
    flowId = params.get('flowId', '')  # 唯一编码
    eventCode = params.get('eventCode', '')  # 事件编码
    flowType = params.get('flowType', '')  # 流转类型 1-下发 2-上报
    flowComment = params.get('flowComment', '')  # 流转备注
    flowUserName = params.get('flowUserName', '')  # 用户名
    flowAppId = params.get('flowAppId', '')  # 关联app
    flowExamine = params.get('flowExamine', '')  # 是否需要审核 0-不需要 1-需要
    flowResult = params.get('flowResult', '')  # 反馈结果
    flowStatus = params.get('flowStatus', '')  # 流转状态 0-未签收 1-签收办理中 2-已办结 4-上报至其他应用于系统系统 5-下发至其他应用系统

    # 修改
    if flowId:
        beacon_eventFlow = EventFlow.objects.filter(flow_id=flowId)
        # 记录不存在
        if not beacon_eventFlow:
            return return_code.RETURN_ERROR
        else:
            app = App.objects.get(code=flowAppId)
            # 执行更新
            beacon_eventFlow.update(event_code=eventCode, flow_type=flowType,flow_comment=flowComment,flow_user_name=flowUserName,flow_app=app,flow_examine=flowExamine,flow_result=flowResult,flow_status=flowStatus)

    # 新增
    else:
        id = uuid.uuid1()
        app = App.objects.get(code=flowAppId)
        beacon_eventFlow = EventFlow(flow_id=id,event_code=eventCode, flow_type=flowType,flow_comment=flowComment,flow_user_name=flowUserName,flow_app=app,flow_examine=flowExamine,flow_result=flowResult,flow_status=flowStatus)
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