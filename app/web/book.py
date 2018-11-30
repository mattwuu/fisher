#!/usr/bin/env python
# encoding: utf-8
"""
@author: Matt.W
@file: book.py
@time: 2018/11/30 5:47
@desc:
"""

from flask import request, jsonify

from app.forms.book import SearchForm
from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.book import Book


@web.route('/book/search')
def search():
    """
    :param q: 普通关键字 or isbn
    :param page:
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = Book.search_by_isbn(q)
        else:
            result = Book.search_by_keyword(q, page)
        # return json.dumps(result), 200, {'content-type': 'application/json'}
        return jsonify(result)
    else:
        return jsonify(form.errors)
