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
from beacon_event.models import *

logger = logging.getLogger('beacon_rpc')


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
            # params = json.loads(request.body)

            # 验证form
            # form = EventUpForm(params)
            # if not form.is_valid():
            #    return error()
            # else:
            # data = params['data']
            # if data:
            data = 'eyJjb21tZW50IjogIjEyMyIsICJzdGF0dXMiOiAxLCAidGFyZ2V0X2lwIjogIjEyMzQiLCAidXNl\
cl9pZCI6IG51bGwsICJmaWxlIjogIiIsICJldmVudF9uYW1lIjogIjEyMyIsICJ1c2VyX25hbWUi\
OiAiMTIzIiwgInNvdXJjZV9pcCI6ICIxMjMiLCAiZGFuZ2VyX2xldmVsIjogMTIzLCAidXJnZW50\
X2xldmVsIjogMTIzLCAidGFyZ2V0X3BvcnQiOiAiMTIzIiwgImV2ZW50X2NvZGUiOiAiMGRkYTM0\
MjMtMjEyMy0xMWU4LWEwNWMtOGM4NTkwNzExYTAzIiwgInRpbWUiOiAiMjAxOC0wMy0wNiAxNzow\
Njo1NiIsICJzb3VyY2VfcG9ydCI6ICIxMjMiLCAidHlwZSI6IDEyMywgImV2ZW50X2Zsb3dzIjog\
W3siZmxvd191c2VyX25hbWUiOiAiYWRtaW4iLCAiZXZlbnRfY29kZSI6ICIwZGRhMzQyMy0yMTIz\
LTExZTgtYTA1Yy04Yzg1OTA3MTFhMDMiLCAiZmxvd190eXBlIjogMSwgImZsb3dfcmVzdWx0Ijog\
IjEiLCAiZmxvd191c2VyX2lkIjogbnVsbCwgImZsb3dfc3RhdHVzIjogMCwgImZsb3dfYXBwX2lk\
IjogIjU0NGVlZTIxLTIxYmItMTFlOC05NjdmLWY4ZGEwYzY0M2NiYyIsICJmbG93X2V4YW1pbmUi\
OiAwLCAiZmxvd19jb21tZW50IjogIjEiLCAiZmxvd19pZCI6ICI1ZDkxMzcyYi0yMWNmLTExZTgt\
YmY0Yy04Yzg1OTA3MTFhMDMiLCAiYWRkX3RpbWUiOiAiMjAxOC0wMy0wNyAxNDoxODozNSJ9LCB7\
ImZsb3dfdXNlcl9uYW1lIjogImFkbWluMSIsICJldmVudF9jb2RlIjogIjBkZGEzNDIzLTIxMjMt\
MTFlOC1hMDVjLThjODU5MDcxMWEwMyIsICJmbG93X3R5cGUiOiAyLCAiZmxvd19yZXN1bHQiOiAi\
MSIsICJmbG93X3VzZXJfaWQiOiBudWxsLCAiZmxvd19zdGF0dXMiOiAwLCAiZmxvd19hcHBfaWQi\
OiAiNTQ0ZWVlMjEtMjFiYi0xMWU4LTk2N2YtZjhkYTBjNjQzY2JjIiwgImZsb3dfZXhhbWluZSI6\
IDAsICJmbG93X2NvbW1lbnQiOiAiMSIsICJmbG93X2lkIjogImE4ZWQwNTk5LTIyNzktMTFlOC04\
ZjQ5LThjODU5MDcxMWEwMyIsICJhZGRfdGltZSI6ICIyMDE4LTAzLTA4IDEwOjM3OjM1In1dLCAi\
YWRkX3RpbWUiOiAiMjAxOC0wMy0wNiAxNzo0NTowNyJ9\
'
            event_json = json.loads(base64.decodestring(data))
            if not event_json:
                return error()
            else:
                event, bool = Event.objects.get_or_create(event_code=event_json['event_code'])
                event.event_name = event_json['event_name']
                event.type = event_json['type']
                event.time = event_json['time']
                event.urgent_level = event_json['urgent_level']
                event.source_ip = event_json['source_ip']
                event.source_port = event_json['source_port']
                event.target_ip = event_json['target_ip']
                event.target_port = event_json['target_port']
                event.danger_level = event_json['danger_level']
                event.comment = event_json['comment']
                event.status = event_json['status']
                event.file = event_json['file']
                event.add_time = event_json['add_time']
                event.user_id = event_json['user_id']
                event.user_name = event_json['user_name']
                event.save()
                if 'event_flows' in event_json:
                    for flow in event_json['event_flows']:
                        event_flow, flow_bool = EventFlow.objects.get_or_create(flow_id=flow['flow_id'])
                        event_flow.event_code = flow['event_code']
                        event_flow.flow_type = flow['flow_type']
                        event_flow.flow_comment = flow['flow_comment']
                        event_flow.flow_user_id = flow['flow_user_id']
                        event_flow.flow_user_name = flow['flow_user_name']
                        event_flow.flow_app = flow['flow_app']
                        event_flow.flow_examine = flow['flow_examine']
                        event_flow.flow_result = flow['flow_result']
                        event_flow.flow_status = flow['flow_status']
                        event_flow.add_time = flow['add_time']
                        event_flow.save()
        return ok(data='ok')

    except Exception as e:
        logger.error(e)
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
