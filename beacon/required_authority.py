#  -*- coding:utf-8 -*-
from django.http import JsonResponse
import json
from beacon_conf import beacon_conf, return_code
from beacon_user.models import Menu


def my_required_authority(function):
    """
    判断用户权限
    :param function:
    :return:
    """

    def wrapper(request, *args, **kw):
        return_data = dict()
        # 已登录,但没有参数
        if not request.body:
            return_data.update(return_code.RETURN_ERROR)
            return JsonResponse(return_data, safe=False)
        # 获取请求参数
        params = json.loads(request.body)
        # 功能函数名
        do_action = params['action']
        if do_action:

            '''
            # 数据库用户类型为测试类型(方便测试使用)
            '''
            if request.user.type:
                return function(request, *args, **kw)

            # 角色
            if request.user.role:
                role_id = request.user.role.id
                actions = Menu.objects.filter(role=role_id, api_action__isnull=False) \
                    .values_list('api_action', flat=True).distinct()
                # 角色存在此权限,或权限不需验证
                if do_action in actions or do_action in beacon_conf.NOT_USER_AUTHORITY_ACTION:
                    return function(request, *args, **kw)
                else:
                    # 无权限
                    return_data.update(return_code.API_REQUEST_NO_AUTHORITY)
                    return JsonResponse(return_data, safe=False)
            else:
                # 无权限
                return_data.update(return_code.API_REQUEST_NO_AUTHORITY)
                return JsonResponse(return_data, safe=False)
        else:
            # 错误
            return_data.update(return_code.RETURN_ERROR)
            return JsonResponse(return_data, safe=False)

    return wrapper
