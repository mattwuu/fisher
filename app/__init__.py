#!/usr/bin/env python
# encoding: utf-8
"""
@author: Matt.W
@file: __init__.py
@time: 2018/11/30 5:48
@desc:
"""

from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
