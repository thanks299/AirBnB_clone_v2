#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask, render_template

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

@app.route("/python/<text>", strict_slashes=False, defaults={"text": "is cool"})
@app.route("/python/<text>/", strict_slashes=False)
def python_text(text):
    text = text.replace("_", " ")
    return "Python " + text

@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_n(n):
    return render_template("number.html", n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even_n(n):
    if n % 2 == 0:
        return render_template("number_odd_or_even.html", n=n, result="even")
    else:
        return render_template("number_odd_or_even.html", n=n, result="odd")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)