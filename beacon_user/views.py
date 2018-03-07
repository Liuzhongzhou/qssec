# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import logging
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from forms import *
from beacon_conf import return_code
from beacon_conf import menu
from models import *
import common

logger = logging.getLogger('beacon_user')


def my_login(request):
    """ 用户登录
    :param request:
    :return:
    """
    context = dict()
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
    if not request.body:
        context.update(return_code.RETURN_ERROR)
        return JsonResponse(context)
    form = LoginForm(json.loads(request.body))
    if not form.is_valid():
        context.update(return_code.API_REQUEST_PARM_ERROR)
        return JsonResponse(context)
    cld = form.cleaned_data
    username = cld['username']
    password = cld['password']

    user = authenticate(username=username, password=password)

    if user is not None:
        if user.is_active:
            login(request, user)
            data = dict()
            data['user_id'] = user.id
            data['user_name'] = user.username
            # 用户等级 0 普遍用户 1 管理员
            data['role'] = user.role_id
            context.update(return_code.RETURN_SUCCESS)
            context['data'] = data
        else:
            logger.error("登录失败,用户不存在")
            context.update(return_code.NO_USER)
    else:
        logger.error("登录失败，用户名或密码错误")
        logger.info("username: {0}".format(username))
        context.update(return_code.USER_PASSWORD_ERROR)
    return JsonResponse(context)


def my_logout(request):
    """ 登出
    :param request:
    :return:
    """
    logout(request)
    return JsonResponse(return_code.RETURN_SUCCESS)


def my_menu(request):
    '''
    获取角色菜单
    :param request:
    :return:
    '''
    params = json.loads(request.body)

    # 验证form
    form = MyMenuForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    user_id = params.get('user_id', '')  # 用户编号
    # 菜单
    menu_lists = menu.MENU_LIST
    list = menu_formart(menu_lists)

    # 获取用户角色
    role = BeaconUser.objects.filter(id=user_id).first().role
    my_menu_codes = Menu.objects.filter(role=role.id).values_list('code', flat=True)

    # 选取用户菜单
    my_list = menu_my_selected(list, my_menu_codes)

    # 返回前端数据
    return_data = dict()
    return_data['data'] = my_list
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def user_list(request):
    """
    用户列表
    :param request:
    :return:
    """
    params = json.loads(request.body)

    # 验证form
    form = UserListForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    user_query_set = BeaconUser.objects.all()
    # 查询条件
    if params['username']:  # 用户名称
        user_query_set = user_query_set.filter(username__icontains=params['username'])
    if params['phone']:  # 电话号
        user_query_set = user_query_set.filter(user_info__phone=params['phone'])
    if params['telephone']:  # 手机号
        user_query_set = user_query_set.filter(user_info__telephone=params['telephone'])

    # 数据查询字段
    sql_keys = ['id', 'username','user_info__chinese_name','user_info__addr','user_info__sex','user_info__telephone','user_info__phone','role__name','org__name']
    # 返回前端字段
    show_keys = ['id', 'username', 'chineseName','addr','sex','telephone','phone','role','org']

    # 获取分页数据
    results = common.get_paginate_data(params, user_query_set, sql_keys, show_keys)

    # 返回前端数据
    return_data = dict()
    return_data['data'] = results
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def user_info(request):
    '''
    查询用户信息
    :param request:
    :return:
    '''
    params = json.loads(request.body)

    # 验证form
    form = UserInfoForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    id = params.get('id', '')  # 编号

    data = dict()
    if id:
        # 数据查询字段
        sql_keys = ['id', 'password', 'username','user_info__chinese_name','user_info__addr','user_info__sex','user_info__telephone','user_info__phone','role__id','org__id']
        show_keys = ['id', 'password', 'username', 'chineseName', 'addr', 'sex', 'telephone', 'phone','role','org']
        # 执行查询
        user_set = BeaconUser.objects.filter(id=id)
        data['user'] = common.transform_array_column(list(user_set.values(*sql_keys)),sql_keys,show_keys)[0]

    # 角色列表
    roleList = list(Role.objects.all().values('id', 'name'))
    data['roleList'] = roleList
    # 组织列表
    orgList = list(Organization.objects.all().values('id', 'name'))
    data['orgList'] = orgList
    # 返回前端数据
    return_data = dict()
    return_data["data"] = data
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def user_save(request):
    '''
    用户编辑
    :param request:
    :return:
    '''
    params = json.loads(request.body)

    # 验证form
    form = UserEditForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    id = params.get('id', '')  # 编号
    username = params.get('username', '')  # 用户名
    password = params.get('password', '')  # 密码
    chineseName = params.get('chineseName', '')  # 姓名
    addr = params.get('addr', '')  # 地址
    sex = params.get('sex', '')  # 性别
    telephone = params.get('telephone', '')  # 电话
    phone= params.get('phone', '')  # 手机
    role_id=params.get('role', '')  # 角色id
    org_id = params.get('org', '')  # 组织id

    # 修改
    if id:
        beacon_user = BeaconUser.objects.filter(id=id)
        # 记录不存在
        if not beacon_user:
            return return_code.RETURN_ERROR
        # 密码加密
        if password and password != beacon_user.first().password:
            password = make_password(password, None)
        user_info_id = beacon_user.values_list('user_info_id')
        user_info = UserInfo.objects.filter(id = user_info_id)
        # 用户角色对象
        role = Role.objects.get(id=role_id)
        # 所属组织对象
        org = Organization.objects.get(id=org_id)
        # 执行更新
        user_info.update(chinese_name=chineseName, addr=addr, sex=sex
                           ,telephone = telephone,phone=phone)
        beacon_user.update(username=username, password=password,role=role,org=org)

    # 新增
    else:
        # 用户名已存在
        if BeaconUser.objects.filter(username=username).last():
            return return_code.USER_NAME_ERROR

        role = Role.objects.get(id=role_id)
        # 所属组织对象
        org = Organization.objects.get(id=org_id)
        # 执行新增
        user_info = UserInfo(chinese_name=chineseName, addr=addr, sex=sex
                           ,telephone = telephone,phone=phone)
        user_info.save()
        user_info_id = user_info.id
        beacon_user = BeaconUser(username=username, password=make_password(password, None),user_info_id= user_info_id,role=role,org=org)
        beacon_user.save()

    # 返回前端数据
    return_data = dict()
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def user_delete(request):
    '''
    删除用户
    :param request:
    :return:
    '''
    params = json.loads(request.body)

    # 验证form
    form = UserDeleteForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    id = params.get('ids', '')  # 编号
    if id:
        user_info_id = BeaconUser.objects.filter(id=id).values_list('user_info_id')
        # 执行删除
        UserInfo.objects.filter(id=user_info_id).delete()
        # 执行删除
        #BeaconUser.objects.filter(id__in=id_list).delete()

    # 返回前端数据
    return_data = dict()
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def role_list(request):
    """
    角色列表
    :param request:
    :return:
    """
    params = json.loads(request.body)

    # 验证form
    form = RoleListForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    role_query_set = Role.objects.all()
    # 查询条件
    if params['name']:  # 角色名称
        role_query_set = role_query_set.filter(name__icontains=params['name'])

    # 数据查询字段
    sql_keys = ['id', 'name', 'comment']

    # 获取分页数据
    results = common.get_paginate_data(params, role_query_set, sql_keys)

    # 返回前端数据
    return_data = dict()
    return_data['data'] = results
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def role_info(request):
    '''
    查询角色信息
    :param request:
    :return:
    '''
    params = json.loads(request.body)

    # 验证form
    form = RoleInfoForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    id = params.get('id', '')  # 编号

    data = dict()
    # 菜单列表
    menu_lists = menu_formart(menu.MENU_LIST)

    if id:
        # 数据查询字段
        sql_keys = ['id', 'name', 'comment']
        # 执行查询
        role_set = Role.objects.filter(id=id)
        data['role'] = role_set.values(*sql_keys).first()
        role_menu_list = role_set.first().menus.all()
        role_menu = []
        for rm in role_menu_list:
            role_menu.append(rm.code)

        # 用户以保存权限
        if role_menu:
            menu_lists = menu_role_selected(menu_lists, role_menu)

    # 返回前端菜单列表
    data['menu_lists'] = menu_lists
    # 返回前端数据
    return_data = dict()
    return_data["data"] = data
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def role_save(request):
    '''
    角色编辑
    :param request:
    :return:
    '''
    params = json.loads(request.body)

    # 验证form
    form = RoleEditForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    id = params.get('id', '')  # 编号
    name = params.get('name', '')  # 角色名
    comment = params.get('comment', '')  # 备注
    menus = params.get('menus', '')  # 菜单列表

    # 修改
    if id:
        role = Role.objects.filter(id=id)
        # 记录不存在
        if not role:
            return return_code.RETURN_ERROR
        # 执行更新
        role.update(name=name, comment=comment)
        role = role.first()
        # 先清除角色没有修改前已保存的菜单
        role.menus.clear()
        # 删除菜单表中冗余数据
        Menu.objects.filter(role__isnull=True).delete()
    # 新增
    else:
        role = Role(name=name, comment=comment)
        # 执行新增
        role.save()

    # 菜单不为空,更新角色所有菜单
    if menus:
        codes = menus.split(',')
        for code in codes:
            # 根据code获取接口action
            actions = get_action_by_code(code)
            if actions:
                # 存在多个接口
                action_list = actions.split(',')
                for action in action_list:
                    Menu.objects.create(code=code, api_action=action, role=role)
            else:
                Menu.objects.create(code=code, role=role)

    # 返回前端数据
    return_data = dict()
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def role_delete(request):
    '''
    删除角色
    :param request:
    :return:
    '''
    params = json.loads(request.body)

    # 验证form
    form = RoleDeleteForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    ids = params.get('ids', '')  # 编号
    # 需删除id数组
    id_list = ids.split(',')

    if id_list:
        # 执行删除
        Role.objects.filter(id__in=id_list).delete()

    # 返回前端数据
    return_data = dict()
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def menu_list(request):
    """
    菜单列表
    :param request:
    :return:
    """
    params = json.loads(request.body)

    # 验证form
    form = MenuListForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    menu_lists = menu.MENU_LIST
    list = menu_formart(menu_lists)
    # 返回前端数据
    return_data = dict()
    return_data['data'] = list
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def menu_formart(list):
    '''
    菜单格式化
    :param list:
    :return:
    '''
    menu_lists = []
    for item in list:
        # 是否展示
        display = item['display']
        if display:
            menu = dict()
            menu['code'] = item['code']
            menu['title'] = item['title']
            if 'children' in item:
                children = menu_formart(item['children'])
                menu['children'] = children
            menu_lists.append(menu)
    return menu_lists


def menu_role_selected(menu_lists, role_menu):
    '''
    勾选角色已存在的菜单
    :param list:
    :return:
    '''
    for item in menu_lists:
        code = item['code']
        if code in role_menu:
            item['checked'] = True
        if 'children' in item:
            menu_role_selected(item['children'], role_menu)
    return menu_lists


def menu_my_selected(menu_lists, my_menu_codes):
    '''
    获取某用户菜单
    :param menu_lists:
    :param my_menu_codes:
    :return:
    '''
    my_menu_list = []
    for item in menu_lists:
        code = item['code']
        menu = dict()
        if 'children' in item:
            children = menu_my_selected(item['children'], my_menu_codes)
            if children:
                menu['children'] = children
        if code in my_menu_codes or 'children' in menu:
            menu['code'] = item['code']
            menu['title'] = item['title']
        if menu:
            my_menu_list.append(menu)
    return my_menu_list


def get_action_by_code(code):
    '''
    根据code获取菜单action
    :param code:
    :return:
    '''
    menu_lists = menu.MENU_LIST
    actions = get_api_action(code, menu_lists)
    return actions


def get_api_action(code, list):
    '''
    根据code获取菜单action
    :param list:
    :return:
    '''
    for item in list:
        if 'action' in item and item['code'] == code:
            return item['action']
        if 'children' in item:
            action = get_api_action(code, item['children'])
            if action:
                return action
    return ''


def organization_list(request):
    """
    组织机构列表
    :param request:
    :return:
    """
    params = json.loads(request.body)

    # 验证form
    form = OrganizationForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    organization_query_list = Organization.objects.values_list('id', 'name', 'pid')
    namelist = []
    for organization in organization_query_list:
        obj = dict()
        obj['id'] = organization[0]
        obj['name'] = organization[1]
        obj['pid'] = organization[2]
        namelist.append(obj)
    # 返回前端数据
    return_data = dict()
    return_data['namelist'] = namelist
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def organization_info(request):
    """
    单个组织机构信息
    :param request:
    :return:
    """
    params = json.loads(request.body)

    # 验证form
    form = OrganizationInfoForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    id = params.get('id', '')  # 编号
    organization = Organization.objects.filter(id=id).first()

    # 返回前端数据
    return_data = dict()
    return_data['organization'] = organization
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def organization_save(request):
    """
    组织机构编辑
    :param request:
    :return:
    """
    params = json.loads(request.body)

    # 验证form
    form = OrganizationSaveForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    id = params.get('id', '')  # 编号
    name = params.get('name', '')  # 组织机构名称
    pid = params.get('pid', '')  # 父ID
    code = params.get('citycode', '')
    city = City.objects.filter(code=code).first()
    city_id = city.id
    # 修改
    if id:
        organization = Organization.objects.filter(id=id)
        # 记录不存在
        if not organization:
            return return_code.RETURN_ERROR
        # 执行更新
        organization.update(name=name, pcode=pid, city_id=city_id)
    # 新增
    else:
        organization = Organization.objects.filter(name=name)
        if organization:
            return return_code.ORGANIZATION_NAME_ERROR
        organization = Organization(name=name, pid=pid, city_id=city_id)
        # 执行新增
        organization.save()
    return_data = dict()
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def organization_delete(request):
    """
    删除组织机构
    :param request:
    :return:
    """
    params = json.loads(request.body)
    # 验证form
    form = OrganizationDelForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    id = params.get('id', '')  # 编号

    if id:
        # 执行删除
        Organization.objects.filter(id=id).delete()
        Organization.objects.filter(pid=id).delete()

    # 返回前端数据
    return_data = dict()
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data


def city_list(request):
    """
        城市列表
        :param request:
        :return:
        """
    params = json.loads(request.body)

    # 验证form
    form = CityForm(params)
    if not form.is_valid():
        return return_code.API_REQUEST_PARM_ERROR

    city_query_list = City.objects.values_list('code', 'name', 'pcode')
    citylist = []
    for city in city_query_list:
        obj = dict()
        obj['value'] = city[0]
        obj['label'] = city[1]
        obj['pcode'] = city[2]
        citylist.append(obj)
    # 返回前端数据
    return_data = dict()
    return_data['citylist'] = citylist
    return_data.update(return_code.RETURN_SUCCESS)
    return return_data



