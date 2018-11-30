#!/usr/bin/env python
# encoding: utf-8
"""
@author: Matt.W
@file: __init__.py
@time: 2018/11/30 5:48
@desc:
"""

from flask import Flask
from app.models.book import db


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    db.init_app(app)
    db.create_all(app=app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
