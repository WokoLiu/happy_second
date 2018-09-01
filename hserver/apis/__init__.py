# -*- coding: utf-8 -*-
# @Time    : 2018/9/1 22:27
# @Author  : Yulong Liu
# @File    : __init__.py

from flask_restful import Api
from .v1_0.days.today import Today


def route_api(app):
    api = Api(app)
    api.add_resource(Today, '/api/v1.0/days', '/api/v1.0/days/<string:date>', endpoint='v1.0.days.today')
