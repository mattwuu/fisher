#!/usr/bin/env python
# encoding: utf-8
"""
@author: Matt.W
@file: book.py
@time: 2018/12/1 3:33
@desc:
"""


class BookViewModel:
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.pages = book['pages']
        self.author = '、'.join(book['author'])
        self.price = book['price']
        self.summary = book['summary']
        self.image = book['image']

    @property
    def intro(self):
        intros = filter(lambda x: True if x else False, [self.author, self.publisher, self.price])
        print(type(intros))
        return ' / '.join(intros)


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, books, keyword):
        self.total = books.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in books.books]


class _BookViewModel:
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
