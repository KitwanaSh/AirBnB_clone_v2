#!/usr/bin/python3
""" Start a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """return 'hello hbnb'
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """return HBNB
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """return a given text
    """
    return "C {}".format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def display(text):
    """ display  text 'Python ',
    followed by the value of the text
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def num_display(n):
    """ display 'n is a number' only"""
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run()
