#!/usr/bin/env python3
"""
This module modifies get_locale function.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """
    Configuration class for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale() -> str:
    """
    Determines best match for supported languages
    Returns:
    str: Best match for supported languages
    """
    locale - request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Renders the index page.
    Returns: str.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
