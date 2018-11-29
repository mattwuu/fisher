from flask import Flask

__author__ = 'Matt.W'

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    return 'Hello Matt'


app.run(host='0.0.0.0', port=81, debug=app.config['DEBUG'])
