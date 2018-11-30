#!/usr/bin/env python
# encoding: utf-8
"""
@author: Matt.W
@file: book.py
@time: 2018/12/1 3:33
@desc:
"""


class BookViewModel:
    @classmethod
    def package_single(cls, data, keyword):
        result = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            result['total'] = 1
            result['books'] = [cls.__get_book_detail(data)]
        return result

    @classmethod
    def package_collection(cls, data, keyword):
        result = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            result['total'] = data['total']
            result['books'] = [cls.__get_book_detail(book) for book in data['books']]
        return result

    @classmethod
    def __get_book_detail(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': '、'.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
