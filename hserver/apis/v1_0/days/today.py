# -*- coding: utf-8 -*-
# @Time    : 2018/9/2 00:23
# @Author  : Yulong Liu
# @File    : today.py

from hlibs.apis import api, response, route
import datetime
from hserver.models.happy.holiday import Holiday


class Today(api.Api):

    def get(self, date=None):
        if date:
            try:
                datetime.datetime.strptime(date, '%Y-%m-%d')
            except ValueError as e:
                return self._return({}, code=400, msg='Date format must be 0001-01-01')
        else:
            date = str(datetime.date.today())

        date_info = Holiday().get_day(date)
        if date_info:
            result = {
                'date': str(date_info['date']),
                'day_type': date_info['day_type'],
                'working_days': date_info['working_days'],
            }
            return self._return(result, code=0, msg='Success')
        else:
            return self._return({}, code=1000, msg='Didn\'t support this date')


if __name__ == '__main__':
    print(datetime.datetime.strptime('2018-09-02', '%Y-%m-%d'))
    print(str(datetime.date.today()))