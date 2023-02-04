#!/usr/bin/python3
""" Initialize the Flask framework
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_world():
    return "Hello HBHB!"


if __name__ == "__main__":
    app.run()
