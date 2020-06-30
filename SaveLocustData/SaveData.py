#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   SaveData.py
 
@Time    :   2020/6/29 2:49 下午
'''


from GetLocustData.GetData import GetData
import time

class SaveData(GetData):

    def __init__(self):
        super().__init__()
        self.test

    @property
    def stats_list(self):
        return self.locustdata.get('stats')

    @property
    def test(self):
        stats_dic = self.stats_list[0]
        self.avg_content_length = stats_dic.get('avg_content_length')
        print(self.avg_content_length)


if __name__ == '__main__':
    print(SaveData())