# -*- coding: utf-8 -*-
# @Time    : 2018/9/2 00:57
# @Author  : Yulong Liu
# @File    : route.py

from flask import current_app
from flask_restful import Api
from functools import wraps


def route(*urls, endpoint=''):
    def outer(func):
        @wraps(func)
        def inner(self, *args, **kwargs):
            print('route', urls, endpoint, args, kwargs)
            api = Api(current_app)
            api.add_resource(self.__class__, *urls, endpoint=endpoint)
            res = func(self, *args, **kwargs)
            return res
        return inner
    return outer

