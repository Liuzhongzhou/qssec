# -*- coding: utf-8 -*-

from django import forms
from beacon.forms import PageForm

# 应用系统列表
class AppListForm(PageForm):
    code = forms.CharField(max_length=50, required=False)
    name = forms.CharField(max_length=128, required=False)
    ip = forms.CharField(max_length=50, required=False)
    city_id = forms.CharField(max_length=256, required=False)
    add_time = forms.DateTimeField(required=False)