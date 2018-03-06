#  -*- coding:utf-8 -*-

"""
返回码说明
1 成功
101 - 199 : 通用返回码
201 - 299 : homeapp 错误码
301 - 399 : userapp 错误码
...
...
"""

RETURN_ERROR = {
    'return_code': 0,
    'message': 'error'
}

RETURN_SUCCESS = {
    'return_code': 1,
    'message': 'success'
}

# ###### 通用返回码 101-199     ######
API_REQUEST_ERROR = {
    'return_code': 101,
    'message': u'接口地址错误'
}

API_REQUEST_USER_ERROR = {
    'return_code': 102,
    'message': u'无效用户'
}

API_REQUEST_METHOD_ERROR = {
    'return_code': 103,
    'message': u'请求方法错误'
}

API_REQUEST_PARM_ERROR = {
    'return_code': 104,
    'message': u'请求参数错误'
}

API_REQUEST_NO_PARAMETER = {
    'return_code': 105,
    'message': u"参数不全"
}

API_REQUEST_NO_AUTHORITY = {
    'return_code': 106,
    'message': u"无访问权限"
}

# ###### userapp返回码 301-399 ######
USER_PASSWORD_ERROR = {
    'return_code': 201,
    'message': u'用户名或密码错误'
}

USER_LOGIN_FAIL = {
    'return_code': 202,
    'message': u'登录失败'
}

# 两次密码不一致
PASSWORD_IS_NOT_PASSWORD2 = {
    'return_code': 203,
    'message': u'两次密码不一致'
}

# 用户名已存在
USER_NAME_ERROR = {
    'return_code': 204,
    'message': u'用户名已存在'
}

# 用户不存在
NO_USER = {
    'return_code': 205,
    'message': u'用户不存在'
}

# 组织机构名称已存在
ORGANIZATION_NAME_ERROR = {
    'return_code': 204,
    'message': u'组织机构名称已存在'
}
