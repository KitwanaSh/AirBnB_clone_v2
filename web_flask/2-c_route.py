#!/usr/bin/python3
""" Starts a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strick_slashes=False)
def hello_world():
    """ return 'hello hbnb'
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """ return HBNB """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """ return a given text
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == "__main__":
    app.run()
