#!/usr/bin/env python
# encoding: utf-8
"""
@author: Matt.W
@file: helper.py
@time: 2018/11/30 2:49
@desc:
"""


def is_isbn_or_key(word):
    """
    :param word: 普通关键字 or isbn
    :return:
    isbn13: 13个0到9的数字组成
    isbn10: 10个0到9数字组成，含有一些'-'
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_q = word.replace('-', '')
    if '-' in word and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key
