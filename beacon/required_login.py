#  -*- coding:utf-8 -*-
from django.http import JsonResponse
import json
from conf import fort_conf, return_code
from beacon.forms import BaseForm


def my_required_login(function):
    """
    判断用户是否登录
    :param function:
    :return:
    """

    def wrapper(request, *args, **kw):
        # 用户已登录,可以执行
        if request.user and request.user.is_authenticated():
            return function(request, *args, **kw)
        # 用户未登录
        else:
            return_data = dict()
            # 判断是否存在请求参数
            if request.body:
                # 获取请求参数
                params = json.loads(request.body)
                form = BaseForm(params)

                # 验证成功
                if form.is_valid():
                    cld = form.cleaned_data
                    action = cld['action']

                    # 不需要登录,可以直接访问
                    if action and action in fort_conf.NOT_USER_LOGIN_ACTION:
                        return function(request, *args, **kw)
                    else:
                        return_data.update(return_code.RETURN_ERROR)
                        return JsonResponse(return_data, safe=False)
                else:  # 验证失败
                    return_data.update(return_code.RETURN_ERROR)
                    return JsonResponse(return_data, safe=False)
            # 无参数,退出请求
            else:
                return_data.update(return_code.RETURN_ERROR)
                return JsonResponse(return_data, safe=False)

    return wrapper
