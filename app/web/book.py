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
from flask_login import current_user

from app.forms.book import SearchForm
from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.book import BookViewModel, BookCollection
from app.view_models.trade import TradeInfo
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
    has_in_gifts = False
    has_in_wishes = False

    books_model = Book()
    books_model.search_by_isbn(isbn)
    book = BookViewModel(books_model.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_wishes_model = TradeInfo(trade_wishes)
    trade_gifts_model = TradeInfo(trade_gifts)

    return render_template('book_detail.html', book=book,
                           wishes=trade_wishes_model,
                           gifts=trade_gifts_model,
                           has_in_wishes=has_in_wishes,
                           has_in_gifts=has_in_gifts)
