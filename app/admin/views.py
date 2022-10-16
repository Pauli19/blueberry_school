"""
This module contains view functions associated with `admin` blueprint.
"""

from flask import render_template
from flask_login import login_required
from sqlalchemy import select

from .. import db
from ..models import Student
from . import admin


@admin.get("/")
@login_required
def index() -> str:
    """View function for "/admin" route when method is GET."""
    return render_template("admin/index.html.jinja")


@admin.get("/student")
@login_required
def student_table() -> str:
    """View function for "/student" route when method is GET."""
    students = (
        db.session.execute(select(Student).order_by(Student.created_at.desc()))
        .scalars()
        .all()
    )

    return render_template("admin/student/table-view.html.jinja", students=students)
