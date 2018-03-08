# -*- coding: utf-8 -*-

from django import forms
from beacon.forms import PageForm

# 事件列表
class EventListForm(PageForm):
    event_name = forms.CharField(max_length=128, required=False)
# 事件信息
class EventInfoForm(forms.Form):
    event_code = forms.CharField(max_length=50)

# 事件删除
class EventDeleteForm(PageForm):
    ids = forms.CharField(max_length=50)

# 事件新增 修改
class EventEditForm(forms.Form):
    event_code = forms.CharField(max_length=50, required=False)
    event_name = forms.CharField(max_length=128)
    type = forms.IntegerField()
    time = forms.DateTimeField()
    urgent_level = forms.IntegerField()
    source_ip = forms.CharField(max_length=20)
    source_port = forms.CharField(max_length=8)
    target_ip = forms.CharField(max_length=20)
    target_port = forms.CharField(max_length=8)
    danger_level = forms.IntegerField()
    comment = forms.CharField(max_length=256)
    status = forms.IntegerField()
    #file = forms.CharField(max_length=256)
    user_name = forms.CharField(max_length=50)

# 事件流转列表
class EventFlowListForm(PageForm):
    flow_user_name = forms.CharField(max_length=50, required=False)

#事件流转信息
class EventFlowInfoForm(forms.Form):
    flow_id = forms.CharField(max_length=50)

#事件流转 新增 修改
class EventFlowEditForm(forms.Form):
    flow_id = forms.CharField(max_length=50, required=False)
    event_code = forms.CharField(max_length=50)
    flow_type = forms.IntegerField()
    flow_comment = forms.CharField(max_length=256)
    flow_user_name = forms.CharField(max_length=50)
    flow_app_id = forms.CharField(max_length=50)
    flow_examine = forms.IntegerField()
    flow_result = forms.CharField(max_length=256)
    flow_status = forms.IntegerField()
