# -*- coding: utf-8 -*-
# @Time    : 2018/9/2 00:01
# @Author  : Yulong Liu
# @File    : response.py

from flask import make_response, jsonify


class Response(object):

    def __init__(self, data=None, code=0, msg=''):
        self.body = {
            'code': code,
            'msg': msg,
            'result': data or None,
        }

    def make_response(self, code=200, headers=None):
        if code > 999 or code < 100:
            code = 200  # 这里的code是 http code
        resp = make_response(jsonify(self.body), code)
        resp.headers.extend(headers or {})
        return resp
