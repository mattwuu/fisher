from app import create_app

__author__ = 'Matt.W'

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81, debug=app.config['DEBUG'])
