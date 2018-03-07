#  -*- coding:utf-8 -*-
from django.http import JsonResponse
from beacon_conf import return_code


def required_rpc(function):
    """
    rpc访问验证
    :param function:
    :return:
    """

    def wrapper(request, *args, **kw):
        # 访问为POST或者GET方式
        if request.method == 'POST' or request.method == 'GET':
            return function(request, *args, **kw)
        else:
            return_data = dict()
            return_data.update(return_code.RETURN_ERROR)
            return JsonResponse(return_data, safe=False)

    return wrapper
