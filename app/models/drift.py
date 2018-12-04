#!/usr/bin/env python
# encoding: utf-8
"""
@author: Matt.W
@file: drift.py
@time: 2018/12/4 10:17
@desc:
"""
from sqlalchemy import Column, Integer, String, SmallInteger

from app.models.base import Base


class Drift(Base):
    """
        一次具体的交易信息
    """
    # __tablename__ = 'drift'

    # def __init__(self):
    #     self.pending = PendingStatus.waiting
    #     super(Drift, self).__init__()

    id = Column(Integer, primary_key=True)
    recipient_name = Column(String(20), nullable=False)
    address = Column(String(100), nullable=False)
    message = Column(String(200))
    mobile = Column(String(20), nullable=False)

    isbn = Column(String(13))
    book_title = Column(String(50))
    book_author = Column(String(30))
    book_img = Column(String(50))

    requester_id = Column(Integer)
    requester_nickname = Column(String(20))

    gifter_id = Column(Integer)
    gift_id = Column(Integer)
    gifter_nickname = Column(String(20))

    pending = Column('pending', SmallInteger, default=1)
    # gift_id = Column(Integer, ForeignKey('gift.id'))
    # gift = relationship('Gift')

    # @property
    # def pending(self):
    #     return PendingStatus(self._pending)
    #
    # @pending.setter
    # def pending(self, status):
    #     self._pending = status.value