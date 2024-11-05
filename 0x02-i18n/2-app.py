#!/usr/bin/env python3
"""
This sets up a Flask app with Babel.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Function for configuring available languages."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localselector
def get_locale():
    """Determines best match for supported languages."""
    return accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Renders home page with welcome message."""
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
