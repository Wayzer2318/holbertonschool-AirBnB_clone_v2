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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def ciscool(text='is cool'):
    """
    python text
    """
    return "Python  " + text.remplace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
    number
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    number template
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """
    number odd or even
    """
    if n % 2 == 0:
        even = "even"
    else:
        even = "odd"
    return render_template('6-number_odd_or_even.html', even=even, n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
