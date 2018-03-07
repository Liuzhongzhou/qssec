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
    role = forms.IntegerField()
    org = forms.IntegerField()


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
