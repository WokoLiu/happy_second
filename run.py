# -*- coding: utf-8 -*-
# @Time    : 2018/9/1 22:39
# @Author  : Yulong Liu
# @File    : run.py

from gevent import monkey
monkey.patch_all()

import os
if not os.environ.get('CONF_ENVIRONMENT'):
    os.environ['CONF_ENVIRONMENT'] = 'product'

from hserver import create_app

app = create_app()

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=4489)
