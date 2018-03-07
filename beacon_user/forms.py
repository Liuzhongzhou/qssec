# -*- coding: utf-8 -*-

from django import forms
from beacon.forms import PageForm


# 用户登录
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=128)


class MyMenuForm(forms.Form):
    user_id = forms.CharField(max_length=20)


# 用户列表
class UserListForm(PageForm):
    username = forms.CharField(max_length=30, required=False)
    phone = forms.CharField(max_length=11, required=False)
    email = forms.CharField(max_length=50, required=False)


# 用户信息
class UserInfoForm(forms.Form):
    id = forms.IntegerField(min_value=0)


# 用户编辑
class UserEditForm(forms.Form):
    id = forms.IntegerField(required=False)
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=128)
    chineseName = forms.CharField(max_length=100)
    addr = forms.CharField(max_length=256)
    sex = forms.IntegerField()
    telephone = forms.CharField(max_length=20)
    phone = forms.CharField(max_length=11)


# 用户删除
class UserDeleteForm(PageForm):
    ids = forms.CharField(max_length=256)


# 角色列表
class RoleListForm(PageForm):
    name = forms.CharField(max_length=30, required=False)


# 角色信息
class RoleInfoForm(forms.Form):
    id = forms.IntegerField(min_value=0)


# 角色编辑
class RoleEditForm(forms.Form):
    id = forms.ImageField(required=False)
    name = forms.CharField(max_length=30)
    comment = forms.CharField(max_length=256)
    menus = forms.CharField(required=False)


# 角色删除
class RoleDeleteForm(PageForm):
    ids = forms.CharField(max_length=256)


# 菜单列表
class MenuListForm(PageForm):
    name = forms.CharField(max_length=30, required=False)


# 组织机构列表
class OrganizationForm(PageForm):
    name = forms.CharField(max_length=128, required=False)
    city = forms.CharField(max_length=128, required=False)


# 组织机构保存
class OrganizationSaveForm(PageForm):
    name = forms.CharField(max_length=128)
    citycode = forms.CharField(max_length=128)
    pid = forms.IntegerField()


# 组织机构详情
class OrganizationInfoForm(PageForm):
    id = forms.IntegerField()


# 组织机构删除
class OrganizationDelForm(PageForm):
    id = forms.IntegerField()


# 城市列表
class CityForm(PageForm):
    code = forms.CharField(max_length=128, required=False)
    name = forms.CharField(max_length=128, required=False)
    type = forms.IntegerField(required=False)
    pcode = forms.CharField(max_length=128, required=False)
