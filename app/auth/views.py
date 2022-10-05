"""
This module contains view functions associated to `auth` blueprint.
"""

from flask import Response, flash, redirect, render_template, url_for
from flask_login import login_required, logout_user

from . import auth
from .forms import LoginForm


@auth.get("/login")
def login_get() -> str:
    """View function for "/login" route."""
    form = LoginForm()
    return render_template("auth/login.html.jinja", form=form)


@auth.get("/logout")
@login_required
def logout() -> Response:
    """View function for "logout" route."""
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("main.index"))
