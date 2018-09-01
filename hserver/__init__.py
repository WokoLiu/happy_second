# -*- coding: utf-8 -*-
# @Time    : 2018/9/1 23:09
# @Author  : Yulong Liu
# @File    : __init__.py

from flask import Flask, make_response, jsonify
from hserver.apis import route_api


def create_app():
    """创建flask应用，并初始化配置"""
    app = Flask(__name__)

    @app.errorhandler(404)
    def not_found(e):
        return make_response(jsonify({'code': 404, 'msg': 'Not Found', 'result': {}}), 404)

    # @app.errorhandler(Exception)
    # def server_error(e):
    #     return make_response(jsonify({'code': 500, 'msg': 'Internal Server Error', 'result': {}}), 500)

    # 引入各个API
    route_api(app)

    return app
