#!/usr/bin/env python3
"""
This module modifies get_locale function.
"""

from flask import Flask, render_template, request
from flask import Babel, _


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['LANGUAGES'] = ['en', 'fr']


babel = Babel(app)


class Config:
    LANGUAGES = ["en", "fr"]


app.config.from_object(Config)


@babel.localselector
def get_locale():
    locale - request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run()
