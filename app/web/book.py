#!/usr/bin/env python
# encoding: utf-8
"""
@author: Matt.W
@file: book.py
@time: 2018/11/30 5:47
@desc:
"""

from flask import jsonify
from . import web
from helper import is_isbn_or_key
from book import Book


@web.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q: 普通关键字 or isbn
    :param page:
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    if isbn_or_key == 'isbn':
        result = Book.search_by_isbn(q)
    else:
        result = Book.search_by_keyword(q)
    # return json.dumps(result), 200, {'content-type': 'application/json'}
    return jsonify(result)
