#!/usr/bin/env python
# encoding: utf-8
'''
@author: Dinner
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hitszluo@gmail.com
@software: pycharm
@file: develop.py
@time: 2020/3/31 20:01
@desc:
'''

from .base import *

DEBUG = True

# 让每部分配置独立开来
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}