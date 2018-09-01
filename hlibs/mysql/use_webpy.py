# -*- coding: utf-8 -*-
# @Time    : 2018/9/2 02:20
# @Author  : Yulong Liu
# @File    : use_webpy.py

import web


def create_engine(dbname, host, port, user, pw, pooling=True):
    db = web.database(dbn="mysql", db=dbname, host=host,
                      port=int(port), user=user,
                      pw=pw, pooling=pooling)
    return db
