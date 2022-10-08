"""
This module contains view functions associated with `auth` blueprint.
"""

from flask import Response, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from sqlalchemy import select

from .. import db
from ..models import User
from . import auth
from .forms import LoginForm


@auth.get("/login")
def login_get() -> str:
    """View function for "/login" route when method is GET."""
    form = LoginForm()
    return render_template("auth/login.html.jinja", form=form)


@auth.post("/login")
def login_post() -> Response:
    """View function for "/login" route when method is POST."""
    form = LoginForm()
    if not form.validate():
        return redirect(url_for("auth.login_get"))

    user: User = db.session.execute(
        select(User).where(
            (User.email == form.email.data) & User.password_hash.is_not(None)
        )
    ).scalar_one_or_none()

    if user is None or not user.verify_password(form.password.data):
        flash("Invalid username or password.", "danger")
        return redirect(url_for("auth.login_get"))

    login_user(user, form.remember_me.data)
    _next = request.args.get("next")
    if _next is None or not _next.startswith("/"):
        _next = url_for("admin.index")

    return redirect(_next)


@auth.get("/logout")
@login_required
def logout() -> Response:
    """View function for "/logout" route."""
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for("main.index"))
