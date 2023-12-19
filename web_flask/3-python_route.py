#!/usr/bin/python3
"""
flask model
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    home
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    hbnb
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def ctext(text):
    """
    c text
    """
    return "C  " + text.remplace("_", " ")


@app.route('/python/<text>', strict_slashes=False)
def pytext(text='is cool'):
    """
    python text
    """
    return "Python  " + text.remplace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
