#!/usr/bin/python3
"""
routes in flask, tasks 1
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hellos HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index1():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def index2(text):
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
