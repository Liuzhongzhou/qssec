# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone


class Event(models.Model):
    '''
    事件
    '''
    event_code = models.CharField(u'唯一编码', max_length=50, primary_key=True)
    # 应用编码
    app_code = models.CharField(u'应用编码', max_length=50)
    event_name = models.CharField(u'事件名称', max_length=128)
    event_type = models.IntegerField(u'事件类型 1-确凿类事件 2-疑似类事件 3-隐患/风险类事件', default=0)
    time = models.DateTimeField(u'发生时间', null=True, blank=True)
    urgent_level = models.IntegerField(u'紧急程度', default=0)
    source_ip = models.CharField(u'源ip', max_length=20, null=True, blank=True)
    source_port = models.CharField(u'源端口', max_length=8, null=True, blank=True)
    target_ip = models.CharField(u'目的', max_length=20, null=True, blank=True)
    target_port = models.CharField(u'目的端口', max_length=8, null=True, blank=True)
    danger_level = models.IntegerField(u'严重等级', default=0)
    comment = models.CharField(u'备注', max_length=256, default='', null=True, blank=True)
    status = models.IntegerField(u'事件状态 0-未签收 1-签收办理中 2-下发办理中 3-上报办理中 4-已办结', default=0)
    file = models.CharField(u'附件', max_length=256, default='', null=True, blank=True)
    add_time = models.DateTimeField(u'创建日期', default=timezone.now)

    # 用户
    user_id = models.IntegerField(u'用户编号', null=True, blank=True)
    user_name = models.CharField(u'用户名', max_length=50)

    class Meta:
        db_table = 't_event'


class EventFlow(models.Model):
    '''
    事件流转
    '''

    flow_id = models.CharField(u'唯一编码', max_length=50, primary_key=True)
    # 应用编码
    app_code = models.CharField(u'应用编码', max_length=50)
    # 关联事件表
    event_code = models.CharField(u'事件编码', max_length=50)

    flow_type = models.IntegerField(u'流转类型 1-下发 2-上报', default=1)
    flow_comment = models.CharField(u'流转备注', max_length=256, default='', blank=True, null=True)
    # 关联用户表
    flow_user_id = models.IntegerField(u'用户编号', null=True, blank=True)
    flow_user_name = models.CharField(u'用户名', max_length=50)
    flow_examine = models.IntegerField(u'是否需要审核 0-不需要 1-需要', default=0)
    flow_result = models.CharField(u'反馈结果', max_length=256, default='', blank=True, null=True)
    flow_status = models.IntegerField(u'流转状态 0-未签收 1-签收办理中 2-已办结 4-上报至其他应用于系统系统 5-下发至其他应用系统', default=0)
    add_time = models.DateTimeField(u'创建日期', default=timezone.now)

    class Meta:
        db_table = 't_event_flow'
