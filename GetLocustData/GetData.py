#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   GetData.py
 
@Time    :   2020/6/29 2:30 下午
'''

import requests
from settings import *


class GetData(object):

    def __init__(self):
        self.s = requests.Session()

    @property
    def locustdata(self):
        r = self.s.get(HOST)
        return r.json()


    @property
    def getdata_f(self):
        import json
        r = self.s.get(HOST)
        r_f = json.dumps(r.json(),indent = 4 , ensure_ascii= False)
        return r_f

if __name__ == '__main__':
    '''
    调用示例
    '''
    class test(GetData):
        def __init__(self):
            super().__init__()
            print(self.locustdata)
    test()