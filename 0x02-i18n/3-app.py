#!/usr/bin/env python3
"""
This module sets up Flask app with babel and localized templates.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """Configuration for available languages."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)


babel = Babel(app)


@babel.localselector
def get_locale():
    """Function determines best match for supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """Function to render homepage with a localized message."""
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
