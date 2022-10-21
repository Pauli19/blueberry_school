"""
This module contains view functions associated with `admin` blueprint.
"""

from flask import Response, flash, redirect, render_template, url_for
from flask_login import login_required
from sqlalchemy import select

from .. import db
from ..models import Class, Cycle, Payment, Representative, Student
from . import admin
from .forms import (
    ClassForm,
    CycleForm,
    PaymentForm,
    RepresentativeCreateForm,
    RepresentativeEditForm,
    StudentCreateForm,
    StudentEditForm,
)


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


@admin.get("/student/create")
@login_required
def create_student_get() -> str:
    """View function for "/student/create" when the method is GET."""
    form = StudentCreateForm()
    return render_template("admin/student/create.html.jinja", form=form)


@admin.post("/student/create")
@login_required
def create_student_post() -> Response:
    """View function for "/student/create" when the method is POST."""
    form = StudentCreateForm()
    if form.validate():
        identity_document = form.identity_document.data
        first_name = form.first_name.data
        second_name = form.second_name.data
        first_surname = form.first_surname.data
        second_surname = form.second_surname.data
        sex = form.sex.data
        birth_date = form.birth_date.data
        email = form.email.data
        phone_number = form.phone_number.data
        representative_id = form.representative.data
        class_id = form.class_.data

        student = Student(
            identity_document=identity_document,
            first_name=first_name,
            second_name=second_name,
            first_surname=first_surname,
            second_surname=second_surname,
            sex=sex,
            birth_date=birth_date,
            email=email,
            phone_number=phone_number,
        )

        if form.representative.data != "" and form.class_.data != "":
            student = Student(
                identity_document=identity_document,
                first_name=first_name,
                second_name=second_name,
                first_surname=first_surname,
                second_surname=second_surname,
                sex=sex,
                birth_date=birth_date,
                email=email,
                phone_number=phone_number,
                representative_id=representative_id,
                class_id=class_id,
            )

        if form.representative.data != "":
            student = Student(
                identity_document=identity_document,
                first_name=first_name,
                second_name=second_name,
                first_surname=first_surname,
                second_surname=second_surname,
                sex=sex,
                birth_date=birth_date,
                email=email,
                phone_number=phone_number,
                representative_id=representative_id,
            )

        if form.class_.data != "":
            student = Student(
                identity_document=identity_document,
                first_name=first_name,
                second_name=second_name,
                first_surname=first_surname,
                second_surname=second_surname,
                sex=sex,
                birth_date=birth_date,
                email=email,
                phone_number=phone_number,
                class_id=class_id,
            )

        session = db.session
        session.add(student)
        session.commit()

        return redirect(url_for("admin.student_table"))

    if form.errors:
        flash(form.errors, "danger")

    return redirect(url_for("admin.create_student_get"))


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


@admin.get("/student/edit/<int:student_id>")
@login_required
def edit_student_get(student_id: int) -> str:
    """View function for "/student/edit/<int:student_id>" when the method is GET."""
    student: Student = db.one_or_404(select(Student).where(Student.id == student_id))
    form = StudentEditForm()
    form.identity_document.data = student.identity_document
    form.first_name.data = student.first_name
    form.second_name.data = student.second_name
    form.first_surname.data = student.first_surname
    form.second_surname.data = student.second_surname
    form.birth_date.data = student.birth_date
    form.sex.data = student.sex.name
    form.email.data = student.email
    form.phone_number.data = student.phone_number.e164
    form.representative.data = student.representative_id
    form.class_.data = student.class_id

    return render_template("admin/student/edit.html.jinja", form=form, student=student)


@admin.post("/student/edit/<int:student_id>")
@login_required
def edit_student_post(student_id: int) -> Response:
    """View function for "/student/edit/<int:student_id>" when the method is POST."""
    form = StudentEditForm()
    student: Student = db.one_or_404(select(Student).where(Student.id == student_id))
    student.identity_document = form.identity_document.data
    student.first_name = form.first_name.data
    student.second_name = form.second_name.data
    student.first_surname = form.first_surname.data
    student.second_surname = form.second_surname.data
    student.birth_date = form.birth_date.data
    student.sex = form.sex.data
    student.email = form.email.data
    student.phone_number = form.phone_number.data
    student.representative_id = form.representative.data
    student.class_id = form.class_.data

    db.session.commit()

    return redirect(url_for("admin.student_table"))


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
    form = RepresentativeCreateForm()
    return render_template("admin/representative/create.html.jinja", form=form)


@admin.post("/representative/create")
@login_required
def create_representative_post() -> Response:
    """View function for "/representative/create" when the method is POST."""
    form = RepresentativeCreateForm()
    if form.validate():
        identity_document = form.identity_document.data
        first_name = form.first_name.data
        second_name = form.second_name.data
        first_surname = form.first_surname.data
        second_surname = form.second_surname.data
        sex = form.sex.data
        email = form.email.data
        phone_number = form.phone_number.data

        representative = Representative(
            identity_document=identity_document,
            first_name=first_name,
            second_name=second_name,
            first_surname=first_surname,
            second_surname=second_surname,
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


@admin.get("/representative/edit/<int:representative_id>")
@login_required
def edit_representative_get(representative_id: int) -> str:
    """
    View function for "/representative/edit/<int:representative_id>"
    when the method is GET.
    """
    representative: Representative = db.one_or_404(
        select(Representative).where(Representative.id == representative_id)
    )
    form = RepresentativeEditForm()
    form.identity_document.data = representative.identity_document
    form.first_name.data = representative.first_name
    form.second_name.data = representative.second_name
    form.first_surname.data = representative.first_surname
    form.second_surname.data = representative.second_surname
    form.sex.data = representative.sex.name
    form.email.data = representative.email
    form.phone_number.data = representative.phone_number.e164

    return render_template(
        "admin/representative/edit.html.jinja",
        representative=representative,
        form=form,
    )


@admin.post("/representative/edit/<int:representative_id>")
@login_required
def edit_representative_post(representative_id: int) -> Response:
    """
    View function for "/representative/edit/<int:representative_id>"
    when the method is POST.
    """
    form = RepresentativeEditForm()
    representative: Representative = db.one_or_404(
        select(Representative).where(Representative.id == representative_id)
    )
    representative.identity_document = form.identity_document.data
    representative.first_name = form.first_name.data
    representative.second_name = form.second_name.data
    representative.first_surname = form.first_surname.data
    representative.second_surname = form.second_surname.data
    representative.sex = form.sex.data
    representative.email = form.email.data
    representative.phone_number = form.phone_number.data

    db.session.commit()

    return redirect(url_for("admin.representative_table"))


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


@admin.get("/cycle/create")
@login_required
def create_cycle_get() -> str:
    """View function for "/cycle/create" when the method is GET."""
    form = CycleForm()
    return render_template("admin/cycle/create.html.jinja", form=form)


@admin.post("/cycle/create")
@login_required
def create_cycle_post() -> Response:
    """View function for "/cycle/create" when the method is POST."""
    form = CycleForm()
    if form.validate():
        month = form.month.data
        year = form.year.data
        start_date = form.start_date.data
        end_date = form.end_date.data

        cycle = Cycle(
            month=month,
            year=year,
            start_date=start_date,
            end_date=end_date,
        )

        session = db.session
        session.add(cycle)
        session.commit()

        return redirect(url_for("admin.cycle_table"))

    if form.errors:
        flash(form.errors, "danger")

    return redirect(url_for("admin.create_cycle_get"))


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


@admin.get("/class/create")
@login_required
def create_class_get() -> str:
    """View function for "/class/create" when the method is GET."""
    form = ClassForm()
    return render_template("admin/class/create.html.jinja", form=form)


@admin.post("/class/create")
@login_required
def create_class_post() -> Response:
    """View function for "/class/create" when the method is POST."""
    form = ClassForm()
    if form.validate():
        mode = form.mode.data
        start_at = form.start_at.data
        end_at = form.end_at.data
        cycle_id = form.cycle.data
        level = form.level.data
        sub_level = form.sub_level.data

        class_ = Class(
            mode=mode,
            start_at=start_at,
            end_at=end_at,
            cycle_id=cycle_id,
            level=level,
            sub_level=sub_level,
        )

        session = db.session
        session.add(class_)
        session.commit()

        return redirect(url_for("admin.class_table"))

    if form.errors:
        flash(form.errors, "danger")

    return redirect(url_for("admin.create_class_get"))


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


@admin.get("/payment/create")
@login_required
def create_payment_get() -> str:
    """View function for "/payment/create" when the method is GET."""
    form = PaymentForm()
    return render_template("admin/payment/create.html.jinja", form=form)


@admin.post("/payment/create")
@login_required
def create_payment_post() -> Response:
    """View function for "/payment/create" when the method is POST."""
    form = PaymentForm()
    if form.validate():
        amount = form.amount.data
        discount = form.discount.data
        description = form.description.data
        student_id = form.student.data
        cycle_id = form.cycle.data

        payment = Payment(
            amount=amount,
            discount=discount,
            description=description,
            student_id=student_id,
            cycle_id=cycle_id,
        )

        session = db.session
        session.add(payment)
        session.commit()

        return redirect(url_for("admin.payment_table"))

    if form.errors:
        flash(form.errors, "danger")

    return redirect(url_for("admin.create_payment_get"))
