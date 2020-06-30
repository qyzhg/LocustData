#!/usr/bin/env python

# -*- encoding: utf-8 -*-

'''
@Author  :   Zhuang_Qingyao
 
@Contact :   qyzhg@163.com
 
@File    :   models.py
 
@Time    :   2020/6/29 4:28 下午
'''

import time
from flask import Flask,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="mysql+pymysql://locust:caini@10.102.17.99:4306/locust"
db = SQLAlchemy(app)

class LocustData(db.Model):
    #主键
    id = db.Column(db.Integer, primary_key=True)
    #项目名
    projectname = db.Column(db.String(80), unique=True)
    #时间戳
    timestamp = db.Column(db.String(80), unique=True)
    #响应时间50线
    current_response_time_percentile_50 = db.Column(db.String(120), unique=False)
    #响应时间95线
    current_response_time_percentile_95 = db.Column(db.String(120), unique=False)
    #错误百分比
    fail_ratio = db.Column(db.String(120), unique=False)
    #总rps
    total_rps = db.Column(db.String(120), unique=False)
    #用户总量
    user_count = db.Column(db.String(120), unique=False)

    def __init__(self,
                 projectname,
                 timestamp,
                 current_response_time_percentile_50,
                 current_response_time_percentile_95,
                 fail_ratio,
                 total_rps,
                 user_count):
        self.projectname = projectname
        self.timestamp = timestamp
        self.current_response_time_percentile_50 = current_response_time_percentile_50
        self.current_response_time_percentile_95 = current_response_time_percentile_95
        self.fail_ratio = fail_ratio
        self.total_rps = total_rps
        self.user_count = user_count
    #
    # def __repr__(self):
    #     return '<User %r>' % self.username

# if __name__ == '__main__':
#     #模型转换数据库
#     db.create_all()

if __name__ == '__main__':
    data1 = LocustData(projectname='test1111',
                       timestamp=str(time.time()),
                       current_response_time_percentile_50=4.5,
                       current_response_time_percentile_95=66.6,
                       fail_ratio=0,
                       total_rps=9,
                       user_count=11)
    db.session.add(data1)