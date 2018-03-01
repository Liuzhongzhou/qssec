# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.utils.timezone as timezone
from django.contrib.auth.models import AbstractUser
from django.db import models


class BeaconUser(AbstractUser):
    '''
    用户
    '''
    user_info = models.OneToOneField('UserInfo', blank=True, null=True)
    # 关联角色表
    role = models.ForeignKey('Role', blank=True, null=True)

    class Meta(AbstractUser.Meta):
        db_table = 'auth_user'


class UserInfo(models.Model):
    chinese_name = models.CharField(u'中文名称', max_length=100)
    img = models.CharField(u'照片', max_length=128)
    sex = models.IntegerField(u'性别 1-男 2-女', default=1)
    phone = models.CharField(u'手机', max_length=11)
    telephone = models.CharField(u'电话', max_length=20)
    idcard = models.CharField(u'身份证号', max_length=18)
    login_type = models.IntegerField(u'登录方式 1-用户名密码 2-USB key 3-短信验证码', default=1)
    comment = models.CharField(u'简介', max_length=256, default='', null=False)
    addr = models.CharField(u'地址', max_length=256, default='', null=False)

    # 用户类型暂时没用
    type = models.IntegerField(u'用户类型', default=0)
    add_time = models.DateTimeField('添加日期', default=timezone.now)

    # 关联组织
    org = models.ForeignKey('Organization', blank=True, null=True)

    class Meta:
        db_table = 't_user_info'


class Role(models.Model):
    '''
    角色
    '''
    name = models.CharField(u'角色名称', max_length=30)
    comment = models.CharField(u'备注', max_length=256, default='', null=False)
    add_time = models.DateTimeField('添加日期', default=timezone.now)

    class Meta:
        db_table = 't_role'


class Menu(models.Model):
    '''
    菜单表
    '''

    code = models.CharField(u"功能编码", max_length=128)
    api_action = models.CharField(u"接口", max_length=128, null=True)
    # 关联角色表
    role = models.ForeignKey('Role', blank=True, null=True, related_name='menus')

    class Meta:
        db_table = 't_role_menu'


class City(models.Model):
    '''
    地市表
    '''
    code = models.CharField(u"地市编码", max_length=128)
    name = models.CharField(u"地市名称", max_length=128)
    type = models.IntegerField(u"地市类型 30-省 40-市 50-区县")
    pcode = models.CharField(u"上级地市编码", max_length=128, blank=True, null=True)

    class Meta:
        db_table = 't_city'


class Organization(models.Model):
    '''
    组织机构
    '''
    name = models.CharField(u"组织名称", max_length=128)
    pid = models.IntegerField(u"父")
    class Meta:
        db_table = 't_organization'
