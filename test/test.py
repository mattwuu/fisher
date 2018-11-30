#!/usr/bin/env python
# encoding: utf-8
"""
@author: Matt.W
@file: test.py
@time: 2018/11/30 22:05
@desc:
"""

from flask import Flask, current_app

app = Flask(__name__)
ctx = app.app_context()
ctx.push()
a = current_app
d = current_app.config['DEBUG']
ctx.pop()

with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']


# 上下文管理器和with语句用法
class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_tb:
            print('process exception')
        else:
            print('no exception')
        print('close resource connection')
        return True

    def query(self):
        print('query data')


with MyResource() as resource:
    resource.query()
