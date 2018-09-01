# -*- coding: utf-8 -*-
# @Time    : 2018/9/1 23:15
# @Author  : Yulong Liu
# @File    : __init__.py

from hlibs.config import config
from . import use_webpy

mysql_info = config._get_config('mysql')


def _get_mysql_conf():
    conf = {}
    for dbname, dbinfo in mysql_info.items():
        conf[dbname] = use_webpy.create_engine(dbname, dbinfo['host'], dbinfo['port'],
                                               dbinfo['user'], dbinfo['pswd'])
    return conf

_mysql_conf = _get_mysql_conf()
