#!/usr/bin/env python
# encoding: utf-8
"""
@author: Matt.W
@file: user.py
@time: 2018/12/1 17:53
@desc:
"""
from sqlalchemy import Column, Integer, String, Boolean, Float
from werkzeug.security import generate_password_hash

from app.models.base import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    _password = Column('password', String(128))
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)
