#!/usr/bin/python3
"""Starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    return "C " + text.replace("_", " ")


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    return "Python " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
"""
    Handles requests to the '/python/' and '/python/<text>' routes.

    Args:
        text (str): The text to be displayed. Defaults to "is cool".

    Returns:
        str: A string containing the text "Python " followed by the input text with underscores replaced by spaces.
    """
def number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
