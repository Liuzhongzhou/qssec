# -*- coding: utf-8 -*-

from django import forms
from beacon.forms import PageForm

# 事件列表
class EventListForm(PageForm):
    eventName = forms.CharField(max_length=128, required=False)
# 事件信息
class EventInfoForm(forms.Form):
    eventCode = forms.CharField(max_length=50)

# 事件删除
class EventDeleteForm(PageForm):
    ids = forms.CharField(max_length=50)

# 事件新增 修改
class EventEditForm(forms.Form):
    eventCode = forms.CharField(max_length=50, required=False)
    eventName = forms.CharField(max_length=128)
    type = forms.IntegerField()
    time = forms.DateTimeField()
    urgentLevel = forms.IntegerField()
    sourceIp = forms.CharField(max_length=20)
    sourcePort = forms.CharField(max_length=8)
    targetIp = forms.CharField(max_length=20)
    targetPort = forms.CharField(max_length=8)
    dangerLevel = forms.IntegerField()
    comment = forms.CharField(max_length=256)
    status = forms.IntegerField()
    #file = forms.CharField(max_length=256)
    userName = forms.CharField(max_length=50)

# 事件流转列表
class EventFlowListForm(PageForm):
    flowUserName = forms.CharField(max_length=50, required=False)

#事件流转信息
class EventFlowInfoForm(forms.Form):
    flowId = forms.CharField(max_length=50)

#事件流转 新增 修改
class EventFlowEditForm(forms.Form):
    flowId = forms.CharField(max_length=50, required=False)
    eventCode = forms.CharField(max_length=50)
    flowType = forms.IntegerField()
    flowComment = forms.CharField(max_length=256)
    flowUserName = forms.CharField(max_length=50)
    flowAppId = forms.CharField(max_length=50)
    flowExamine = forms.IntegerField()
    flowResult = forms.CharField(max_length=256)
    flowStatus = forms.IntegerField()
