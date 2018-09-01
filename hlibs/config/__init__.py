# -*- coding: utf-8 -*-
# @Time    : 2018/9/2 02:43
# @Author  : Yulong Liu
# @File    : __init__.py.py

from . import config

_GLOBLE_CONF = {}


def get_globle_conf(conf):
    global _GLOBLE_CONF
    if _GLOBLE_CONF.get(conf) is not None:
        return _GLOBLE_CONF[conf]
    else:
        conf_info = config._get_config(conf)
        _GLOBLE_CONF[conf] = conf_info
        return conf_info
