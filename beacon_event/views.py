# -*- coding: utf-8 -*-

from beacon_conf import return_code
from django.http import JsonResponse


def eveln_file(request):
    '''
    文件上传
    :param request:
    :return:
    '''
    print '111111111111111111'

    return_data = dict()
    return_data['data'] = ''
    return_data.update(return_code.RETURN_SUCCESS)
    return JsonResponse(return_data, safe=False)
