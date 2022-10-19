"""
This module contains view functions associated with `admin` blueprint.
"""

from flask import Response, flash, redirect, render_template, url_for
from flask_login import login_required
from sqlalchemy import select

from .. import db
from ..models import Class, Cycle, Payment, Representative, Student
from . import admin
from .forms import RepresentativeForm


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


@admin.get("/student/<int:student_id>")
@login_required
def student_view(student_id: int) -> str:
    """View function for "/student/<int:student_id>" route when method is GET."""
    student = db.one_or_404(select(Student).where(Student.id == student_id))
    representative = student.representative
    class_ = student.class_
    return render_template(
        "admin/student/student.html.jinja",
        student=student,
        representative=representative,
        class_=class_,
    )


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


@admin.get("/representative/create")
@login_required
def create_representative_get() -> str:
    """View function for "/representative/create" when the method is GET."""
    form = RepresentativeForm()
    return render_template("admin/representative/create.html.jinja", form=form)


@admin.post("/representative/create")
@login_required
def create_representative_post() -> Response:
    """View function for "/representative/create" when the method is POST."""
    form = RepresentativeForm()
    if form.validate():
        identity_document = form.identity_document.data
        first_name = form.first_name.data
        second_name = form.second_name.data
        first_surname = form.first_surname.data
        sex = form.sex.data
        email = form.email.data
        phone_number = form.phone_number.data

        representative = Representative(
            identity_document=identity_document,
            first_name=first_name,
            second_name=second_name,
            first_surname=first_surname,
            sex=sex,
            email=email,
            phone_number=phone_number,
        )

        session = db.session
        session.add(representative)
        session.commit()

        return redirect(url_for("admin.representative_table"))

    if form.errors:
        flash(form.errors, "danger")

    return redirect(url_for("admin.create_representative_get"))


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


@admin.get("/class/<int:class_id>")
@login_required
def class_view(class_id: int) -> str:
    """View function for "/class/<int:class_id>" route when the method is GET."""
    class_: Class = db.one_or_404(select(Class).where(Class.id == class_id))
    cycle = class_.cycle
    students = class_.students
    return render_template(
        "admin/class/class.html.jinja", class_=class_, cycle=cycle, students=students
    )


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
