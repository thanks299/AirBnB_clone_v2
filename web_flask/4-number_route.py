#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False, defaults={"text": "is cool"})
@app.route("/c/<text>/", strict_slashes=False)
def c_text(text):
    text = text.replace("_", " ")
    return "C " + text


@app.route("/python/", strict_slashes=False, defaults={"text": "is cool"})
@app.route("/python/<text>/", strict_slashes=False)
def fl_python(text="is cool"):
    text = text.replace("_", " ")
    return "Python " + text


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
