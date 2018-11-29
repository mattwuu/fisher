from flask import Flask
from flask.json import jsonify

from helper import is_isbn_or_key
from book import Book

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
    if isbn_or_key == 'isbn':
        result = Book.search_by_isbn(q)
    else:
        result = Book.search_by_keyword(q)
    # return json.dumps(result), 200, {'content-type': 'application/json'}
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=app.config['DEBUG'])
