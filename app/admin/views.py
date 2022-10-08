"""
This module contains view functions associated with `admin` blueprint.
"""

from flask import render_template
from flask_login import login_required

from . import admin


@admin.get("/")
@login_required
def index() -> str:
    """View function for "/admin" route when method is GET."""
    return render_template("admin/index.html.jinja")
