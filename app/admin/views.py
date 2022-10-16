"""
This module contains view functions associated with `admin` blueprint.
"""

from flask import render_template
from flask_login import login_required
from sqlalchemy import select

from .. import db
from ..models import Class, Cycle, Payment, Representative, Student
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


@admin.get("/representative")
@login_required
def representative_table() -> str:
    """View function for "/representative" route when method is GET."""
    representatives = (
        db.session.execute(
            select(Representative).order_by(Representative.created_at.desc())
        )
        .scalars()
        .all()
    )

    return render_template(
        "admin/representative/table-view.html.jinja", representatives=representatives
    )


@admin.get("/cycle")
@login_required
def cycle_table() -> str:
    """View function for "/cycle" route when method is GET."""
    cycles = (
        db.session.execute(select(Cycle).order_by(Cycle.created_at.desc()))
        .scalars()
        .all()
    )

    return render_template(
        "admin/cycle/table-view.html.jinja",
        cycles=cycles,
    )


@admin.get("/class")
@login_required
def class_table() -> str:
    """View function for "/class" route when method is GET."""
    classes = (
        db.session.execute(select(Class).order_by(Class.created_at.desc()))
        .scalars()
        .all()
    )

    return render_template("admin/class/table-view.html.jinja", classes=classes)


@admin.get("/payment")
@login_required
def payment_table() -> str:
    """View function for "/payment" route when method is GET."""
    payments = (
        db.session.execute(select(Payment).order_by(Payment.created_at.desc()))
        .scalars()
        .all()
    )

    return render_template("admin/payment/table-view.html.jinja", payments=payments)
