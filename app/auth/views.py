"""
This module contains view functions associated to `auth` blueprint.
"""

from flask import render_template

from . import auth
from .forms import LoginForm


@auth.get("/login")
def login_get() -> str:
    """View function for "/login" route."""
    form = LoginForm()
    return render_template("auth/login.html.jinja", form=form)
