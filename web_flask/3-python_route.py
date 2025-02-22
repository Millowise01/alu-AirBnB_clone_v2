#!/usr/bin/python3
"""A Flask web application with multiple routes"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Handles requests to the root URL ('/').

    Returns:
        str: A string containing the greeting message "Hello HBNB!".
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Handles requests to the '/hbnb' route.

    Returns:
        str: A string containing the message "HBNB".
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Handles requests to the '/c/<text>' route.

    Args:
        text (str): The text to be displayed.

    Returns:
        str: A string containing the text "C " followed by the input text with underscores replaced by spaces.
    """
    return "C " + text.replace("_", " ")


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """
    Handles requests to the '/python/' and '/python/<text>' routes.

    Args:
        text (str): The text to be displayed. Defaults to "is cool".

    Returns:
        str: A string containing the text "Python " followed by the input text with underscores replaced by spaces.
    """
    return "Python " + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
