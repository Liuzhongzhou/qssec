# -*- coding: utf-8 -*-

from django import forms


# app列表
class AppListForm(forms.Form):
    data = forms.CharField(max_length=256)
