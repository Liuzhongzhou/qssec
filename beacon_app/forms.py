# -*- coding: utf-8 -*-

from django import forms
from beacon.forms import PageForm


# 应用系统列表
class AppListForm(PageForm):
    app_code = forms.CharField(max_length=50, required=False)
    app_name = forms.CharField(max_length=128, required=False)
    app_ip = forms.CharField(max_length=50, required=False)
    app_port = forms.CharField(max_length=50, required=False)
    city_code = forms.CharField(max_length=256, required=False)
    add_time = forms.DateTimeField(required=False)
