# -*- coding: utf-8 -*-
# @Time    : 2018/9/2 02:43
# @Author  : Yulong Liu
# @File    : config.py

from configparser import ConfigParser
import os


def _get_config(file_name):
    conf = ConfigParser()
    file_path = 'hconf/' + os.environ.get('CONF_ENVIRONMENT') + '/' + file_name + '.ini'
    conf.read(file_path, encoding='utf-8')
    sections = conf.sections()
    if not sections:
        return {}
    section_dict = {}
    for section in sections:
        conf_dict = {}
        for k, v in conf.items(section):
            conf_dict[k] = v
        section_dict[section] = conf_dict
    return section_dict

