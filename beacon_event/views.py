# -*- coding: utf-8 -*-

from beacon_conf import return_code, mongodb
from django.http import JsonResponse
import bson.binary
from pymongo import MongoClient
from cStringIO import StringIO
import uuid


def upload_file(request):
    client = MongoClient(mongodb.MongodbInfo['ip'], mongodb.MongodbInfo['port'])
    # 获得一个database
    db = client.MongoFile
    # 获得一个collection
    coll = db.image
    # 获取文件对象
    file = request.FILES.get("file", None)
    # 获取文件名称
    filename = str(request.FILES['file'])
    content = StringIO(file.read())
    # 保存
    coll.save(dict(
        content=bson.binary.Binary(content.getvalue()),
        filename=filename,
        id=uuid.uuid1()
    ))
    # 返回前端数据
    return_data = dict()
    return_data.update(return_code.RETURN_SUCCESS)
    return JsonResponse(return_data, safe=False)


# def getFile():
#     client = MongoClient('192.168.12.37', 27017)
#     # 获得一个database
#     db = client.MongoFile
#     # 获得一个collection
#     coll = db.image
#     data = coll.find_one({'filename': 'titanic_train.sql'})
#     out = open('/Users/xiong/Desktop/777.txt'.decode('utf-8'), 'wb')
#     out.write(data['content'])
#     out.close()
#     print "读取成功！！！"