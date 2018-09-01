# -*- coding: utf-8 -*-
# @Time    : 2018/9/1 23:56
# @Author  : Yulong Liu
# @File    : api.py

from flask_restful import Resource
from hlibs.apis import response


class Api(Resource):
    """业务API类的父类"""
    def _return(self, data, code=0, msg='', headers=None):
        resp = response.Response(data, code, msg)
        return resp.make_response(code)


