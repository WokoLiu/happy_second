# -*- coding: utf-8 -*-
# @Time    : 2018/9/2 02:14
# @Author  : Yulong Liu
# @File    : holiday.py

from hlibs.mysql import _mysql_conf


class Holiday(object):

    def __init__(self):
        self.db = _mysql_conf['happy']
        self.table = 'holiday'

    def get_day(self, date):
        """获取某一天"""
        res = self.db.where(self.table, date=date, status=1)
        if res:
            return dict(res[0])
        else:
            return {}
