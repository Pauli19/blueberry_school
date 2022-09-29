"""
This module contains view functions associated to `main` blueprint.
"""

from flask import render_template

from . import main


@main.get("/")
def index() -> str:
    """View function for "/" route."""
    return render_template("index.html.jinja")
