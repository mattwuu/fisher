from flask import Flask
from helper import is_isbn_or_key

__author__ = 'Matt.W'

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    """
    :param q: 普通关键字 or isbn
    :param page:
    :return:
    """
    isbn_or_key = is_isbn_or_key(q)
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=app.config['DEBUG'])
