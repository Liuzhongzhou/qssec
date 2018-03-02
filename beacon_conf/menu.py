#  -*- coding:utf-8 -*-
'''
菜单列表
code - 菜单编码
title - 菜单名称
icon - 菜单图标
type - 菜单类型 1-菜单 2-功能
display - 是否在前段显示
action - api接口 多个以,隔开
'''
MENU_LIST = [
    {"code": "010000", "title": "首页", "icon": "home", "type": "1", "display": True},
    {"code": "020000", "title": "用户", "icon": "user", "type": "1", "display": True,
     "children": [
         {"code": "010001", "title": "列表", "icon": "userList", "type": "2", "display": True, "action": "user_list"},
         {"code": "010002", "title": "新增", "icon": "userEdit", "type": "2", "display": True,
          "action": "user_info,user_edit"},
         {"code": "010003", "title": "编辑", "icon": "userEdit", "type": "2", "display": True,
          "action": "user_info,user_edit"},
         {"code": "010004", "title": "删除", "icon": "userDelete", "type": "2", "display": True, "action": "user_delete"},
     ]},
    {"code": "030000", "title": "角色", "icon": "role", "type": "菜单", "display": True,
     "children": [
         {"code": "030001", "title": "列表", "icon": "userList", "type": "2", "display": True, "action": "role_list"},
         {"code": "030002", "title": "新增", "icon": "userEdit", "type": "2", "display": True,
          "action": "role_info,role_edit"},
         {"code": "030003", "title": "编辑", "icon": "userEdit", "type": "2", "display": True,
          "action": "role_info,role_edit"},
         {"code": "030004", "title": "删除", "icon": "userDelete", "type": "2", "display": True, "action": "role_delete"},
     ]},
    {"code": "050000", "title": "组织机构", "icon": "organization", "type": "菜单", "display": True,
        "children": [
         {"code": "050001", "title": "列表", "icon": "organizationList", "type": "2", "display": True, "action": "organization_list"},
         {"code": "050002", "title": "新增", "icon": "organizationEdit", "type": "2", "display": True,
          "action": "organization_info,organization_edit"},
         {"code": "050003", "title": "编辑", "icon": "organizationEdit", "type": "2", "display": True,
          "action": "organization_info,organization_edit"},
         {"code": "050004", "title": "删除", "icon": "organizationDelete", "type": "2", "display": True, "action": "organization_delete"},
    ]}
]
