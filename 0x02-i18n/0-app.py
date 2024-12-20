#!/usr/bin/env python3
"""
This module sets up a basic flask module.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """This function renders home page with welcome message."""
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
