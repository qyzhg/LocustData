#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   settings.py
 
@Time    :   2020/6/29 10:43 上午
'''

import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#locust的地址
HOST = 'http://10.102.17.226:8089/stats/requests'