#  -*- coding:utf-8 -*-

from django.http import JsonResponse
import json
import action
import logging
import required_login
import required_authority
from beacon_conf import return_code

logger = logging.getLogger('beacon')


@required_login.my_required_login
@required_authority.my_required_authority
def home(request):
    # 获取请求参数
    params = json.loads(request.body)
    do_action = params['action']  # 功能函数名

    func = getattr(action, do_action, None)

    # 接口不存在
    if not func:
        return_data = dict()
        return_data.update(return_code.API_REQUEST_METHOD_ERROR)
        return JsonResponse(return_data, safe=False)

    setattr(request, 'action', do_action)
    return_data = func(request)

    # logger.info('==return_code:', str(return_data['return_code']), '.params:', params)
    return JsonResponse(return_data, safe=False)
