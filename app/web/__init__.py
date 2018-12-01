#!/usr/bin/env python
# encoding: utf-8
"""
@author: Matt.W
@file: __init__.py
@time: 2018/11/30 5:49
@desc:
"""

from flask import Blueprint

web = Blueprint('web', __name__)

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
