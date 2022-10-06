"""
This module contains view functions associated with `auth` blueprint.
"""

from flask import Response, flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from app.models import User

from . import auth
from .forms import LoginForm


@auth.get("/login")
def login_get() -> str:
    """View function for "/login" route when method is GET."""
    form = LoginForm()
    return render_template("auth/login.html.jinja", form=form)


@auth.post("/login")
def login_post():
    """View function for "/login" route when method is POST."""
    form = LoginForm()
    if not form.validate():
        return redirect(url_for("auth.login_get"))

    user: User = User.query.filter(
        User.email == form.email.data, User.password_hash.is_not(None)
    ).first()

    if user is None or not user.verify_password(form.password.data):
        flash("Invalid username or password.", "danger")
        return redirect(url_for("auth.login_get"))

    login_user(user, form.remember_me.data)
    return redirect(url_for("admin.index"))


@auth.get("/logout")
@login_required
def logout() -> Response:
    """View function for "/logout" route."""
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("main.index"))
