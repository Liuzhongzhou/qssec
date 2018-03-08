# -*- coding: utf-8 -*-

from django import forms


# app列表
class AppListForm(forms.Form):
    data = forms.CharField()


# 事件上传
class EventUpForm(forms.Form):
    data = forms.CharField()
