#!/usr/bin/env python
# encoding: utf-8
"""
@author: Matt.W
@file: book.py
@time: 2018/11/30 5:47
@desc:
"""
import json

from flask import request, jsonify, flash, render_template

from app.forms.book import SearchForm
from app.view_models.book import BookViewModel, BookCollection
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
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        book = Book()
        isbn_or_key = is_isbn_or_key(q)

        if isbn_or_key == 'isbn':
            book.search_by_isbn(q)
        else:
            book.search_by_keyword(q, page)

        books.fill(book, q)
        # return json.dumps(books, default=lambda o: o.__dict__)
        # return jsonify(books.__dict__)
    else:
        flash('搜索的关键字不符合要求，请重新输入关键字')
        # return jsonify(form.errors)
    return render_template('search_result.html', books=books, form=form)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    pass
