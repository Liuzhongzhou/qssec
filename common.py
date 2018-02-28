#  -*- coding:utf-8 -*-

def get_paginate_data(params, query_set, sql_keys=None, show_keys=None):
    """
    封装分页对象
    :param params: django的参数
    :param query_set: django model的query set或者其他list like objects
    :param sql_keys: 查询sql字段
    :param show_keys: 返回前端字段
    :return:
    """
    try:
        pageSize = int(params.get('pageSize', 10))
    except ValueError:
        pageSize = 10
    if pageSize < 0 or pageSize > 100:
        pageSize = 10
    try:
        curPage = int(params.get('curPage', 1))
    except ValueError:
        curPage = 1
    if curPage <= 0:
        curPage = 1

    offset = (curPage - 1) * pageSize
    if sql_keys:
        results = list(query_set.values(*sql_keys)[offset:offset + pageSize])
    else:
        results = list(query_set.values()[offset:offset + pageSize])

    if sql_keys and show_keys:
        results = transform_array_column(results, sql_keys, show_keys)

    page = dict()
    page['totalCount'] = query_set.count()
    page['curPage'] = curPage
    page['pageSize'] = pageSize

    data = {"list": results, "page": page}
    return data


def transform_array_column(list, old_column, new_column):
    """
    转换数组中列的别名
    :param params: list
    :param params: old_column
    :param params: old_column
    :return:
    """
    data = []
    for x in list:
        tmp = dict()
        for i in range(len(old_column)):
            tmp[new_column[i]] = x[old_column[i]]
        data.append(tmp)
    return data

def parse_js(expr):
    """
    解析非标准JSON的Javascript字符串，等同于json.loads(JSON str)
    :param expr:非标准JSON的Javascript字符串
    :return:Python字典
    """
    import ast
    m = ast.parse(expr)
    a = m.body[0]

    def parse(node):
        if isinstance(node, ast.Expr):
            return parse(node.value)
        elif isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.Str):
            return node.s
        elif isinstance(node, ast.Name):
            return node.id
        elif isinstance(node, ast.Dict):
            return dict(zip(map(parse, node.keys), map(parse, node.values)))
        elif isinstance(node, ast.List):
            return map(parse, node.elts)
        else:
            raise NotImplementedError(node.__class__)

    return parse(a)
