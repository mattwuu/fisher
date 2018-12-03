#!/usr/bin/env python
# encoding: utf-8
"""
@author: Matt.W
@file: wish.py
@time: 2018/12/4 0:53
@desc:
"""

from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.models.base import Base


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    uid = Column(Integer, ForeignKey('user.id'))
    # book = relationship('Book')
    # bid = Column(Integer, ForeignKey('book.id'), nullable=False)
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)
