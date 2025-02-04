#!/usr/bin/python3
"""
script that starts a Flask web application:
"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Function that display Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Function that display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """Function that display C {text}"""
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
