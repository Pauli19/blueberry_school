"""
This module contains view functions associated with the
Blueprint `main`.
"""

from flask import render_template

from . import main


@main.get("/")
def index() -> str:
    """View function for "/" route."""
    return render_template("index.html.jinja")
