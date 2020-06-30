#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   app.py
 
@Time    :   2020/6/29 3:35 下午
'''

import time
from flask import Flask,request
from App.models import db,LocustData


app = Flask(__name__)

def insert_data():
    data = LocustData(projectname='test1111',
                      timestamp=str(time.time()),
                      current_response_time_percentile_50=4.5,
                      current_response_time_percentile_95=66.6,
                      fail_ratio=0,
                      total_rps=9,
                      user_count=11)
    db.session.add(data)
    db.session.commit()

if __name__ == '__main__':
    print(LocustData.query.filter_by(projectname='test1111').first().projectname)