"""
This module contains view functions associated to `auth` blueprint.
"""

from flask import render_template

from . import auth


@auth.get("/login")
def login() -> str:
    """View function for "/login" route."""
    return render_template("auth/login.html.jinja")
