"""This module contains forms for `admin` blueprint."""

from typing import Any

from flask_wtf import FlaskForm
from markupsafe import Markup
from sqlalchemy import select
from wtforms import (
    DateField,
    DateTimeField,
    DecimalField,
    EmailField,
    IntegerField,
    SelectField,
    StringField,
    SubmitField,
    TelField,
    TextAreaField,
)
from wtforms.validators import Email, InputRequired, NumberRange

from .. import db
from ..models import (
    Class,
    Cycle,
    Level,
    Mode,
    Month,
    Representative,
    Sex,
    Student,
    SubLevel,
)


class DeleteButtonWidget:  # pylint: disable=too-few-public-methods
    """This class represents a custom delete button widget."""

    def __call__(self, field: SubmitField, **kwargs: Any) -> Markup:
        style = "padding: 0;border: none;background:none;"
        html = (
            f'<button id={field.name} class="text-dark" style="{style}">'
            '<i class="bi bi-trash"></i></button>'
        )
        return Markup(html)


class RepresentativeFormMixin(FlaskForm):
    """This class is a mixin form for a representative."""

    identity_document = StringField("Identity Document", validators=[InputRequired()])
    first_name = StringField("First Name", validators=[InputRequired()])
    second_name = StringField("Second Name")
    first_surname = StringField("First Surname", validators=[InputRequired()])
    second_surname = StringField("Second Surname")
    sex = SelectField(
        "Sex",
        choices=[
            ("", "---"),
            (Sex.FEMALE.name, Sex.FEMALE.value),
            (Sex.MALE.name, Sex.MALE.value),
        ],
    )
    email = EmailField("Email", validators=[Email()])
    phone_number = TelField("Phone Number", validators=[InputRequired()])


class RepresentativeCreateForm(RepresentativeFormMixin):
    """This class represents a form to create a representative."""

    submit = SubmitField("Create")


class RepresentativeEditForm(RepresentativeFormMixin):
    """This class represents a form to edit a representative."""

    submit = SubmitField("Save")


class StudentFormMixin(FlaskForm):
    """This class is a mixin form for a a student."""

    identity_document = StringField("Identity Document", validators=[InputRequired()])
    first_name = StringField("First Name", validators=[InputRequired()])
    second_name = StringField("Second Name")
    first_surname = StringField("First Surname", validators=[InputRequired()])
    second_surname = StringField("Second Surname")
    sex = SelectField(
        "Sex",
        choices=[
            ("", "---"),
            (Sex.FEMALE.name, Sex.FEMALE.value),
            (Sex.MALE.name, Sex.MALE.value),
        ],
        validators=[InputRequired()],
    )
    birth_date = DateField("Birth Date", validators=[InputRequired()])
    email = EmailField("Email", validators=[Email()])
    phone_number = TelField("Phone Number", validators=[InputRequired()])
    representative = SelectField("Representative")
    class_ = SelectField("Class")

    def __init__(self) -> None:
        super().__init__()
        representative_choices = [("", "No representative")]
        representative_choices.extend(
            [
                (representative.id, str(representative))
                for representative in (
                    db.session.execute(
                        select(Representative).order_by(
                            Representative.created_at.desc()
                        )
                    )
                    .scalars()
                    .all()
                )
            ]
        )
        self.representative.choices = representative_choices

        class_choices = [("", "No class")]
        class_choices.extend(
            [
                (class_.id, str(class_))
                for class_ in (
                    db.session.execute(select(Class).order_by(Class.created_at.desc()))
                    .scalars()
                    .all()
                )
            ]
        )
        self.class_.choices = class_choices


class StudentCreateForm(StudentFormMixin):
    """This class represents a form to create a student."""

    submit = SubmitField("Create")


class StudentEditForm(StudentFormMixin):
    """This class represents a form to edit a student."""

    submit = SubmitField("Save")


class CycleForm(FlaskForm):
    """This class represents a form to create a cycle."""

    month = SelectField(
        "Month",
        choices=[
            ("", "---"),
            (Month.JANUARY.name, Month.JANUARY.value),
            (Month.FEBRUARY.name, Month.FEBRUARY.value),
            (Month.MARCH.name, Month.MARCH.value),
            (Month.APRIL.name, Month.APRIL.value),
            (Month.MAY.name, Month.MAY.value),
            (Month.JUNE.name, Month.JUNE.value),
            (Month.JULY.name, Month.JULY.value),
            (Month.AUGUST.name, Month.AUGUST.value),
            (Month.SEPTEMBER.name, Month.SEPTEMBER.value),
            (Month.OCTOBER.name, Month.OCTOBER.value),
            (Month.NOVEMBER.name, Month.NOVEMBER.value),
            (Month.DECEMBER.name, Month.DECEMBER.value),
        ],
        validators=[InputRequired()],
    )
    year = IntegerField("Year", validators=[InputRequired(), NumberRange(min=2022)])
    start_date = DateField("Start Date", validators=[InputRequired()])
    end_date = DateField("End Date", validators=[InputRequired()])
    submit = SubmitField("Create")


class ClassForm(FlaskForm):
    """This class represents a form to create a class for students."""

    mode = SelectField(
        "Mode",
        choices=[
            ("", "---"),
            (Mode.NORMAL.name, Mode.NORMAL.value),
            (Mode.INTENSIVE.name, Mode.INTENSIVE.value),
        ],
        validators=[InputRequired()],
    )
    start_at = DateTimeField("Start At", format="%H:%M", validators=[InputRequired()])
    end_at = DateTimeField("End At", format="%H:%M", validators=[InputRequired()])
    cycle = SelectField("Cycle", validators=[InputRequired()])
    level = SelectField(
        "Level",
        choices=[
            ("", "---"),
            (Level.L1.name, Level.L1.value),
            (Level.L2.name, Level.L2.value),
            (Level.L3.name, Level.L3.value),
        ],
        validators=[InputRequired()],
    )
    sub_level = SelectField(
        "SubLevel",
        choices=[
            ("", "---"),
            (SubLevel.P1.name, SubLevel.P1.value),
            (SubLevel.P2.name, SubLevel.P2.value),
            (SubLevel.P3.name, SubLevel.P3.value),
            (SubLevel.P4.name, SubLevel.P4.value),
        ],
        validators=[InputRequired()],
    )
    submit = SubmitField("Create")

    def __init__(self) -> None:
        super().__init__()
        cycle_choices = [("", "---")]
        cycle_choices.extend(
            [
                (cycle.id, str(cycle))
                for cycle in (
                    db.session.execute(select(Cycle).order_by(Cycle.created_at.desc()))
                    .scalars()
                    .all()
                )
            ]
        )
        self.cycle.choices = cycle_choices


class PaymentForm(FlaskForm):
    """This class represents a form to create a payment."""

    amount = DecimalField(
        "Amount",
        places=2,
        rounding=None,
        validators=[InputRequired(), NumberRange(min=0.01)],
    )
    discount = DecimalField(
        "Discount", default=0, places=2, rounding=None, validators=[NumberRange(min=0)]
    )
    description = TextAreaField("Description")
    student = SelectField("Student")
    cycle = SelectField("Cycle")
    submit = SubmitField("Create")

    def __init__(self) -> None:
        super().__init__()
        student_choices = [("", "---")]
        student_choices.extend(
            [
                (student.id, str(student))
                for student in (
                    db.session.execute(
                        select(Student).order_by(Student.created_at.desc())
                    )
                    .scalars()
                    .all()
                )
            ]
        )
        self.student.choices = student_choices

        cycle_choices = [("", "---")]
        cycle_choices.extend(
            [
                (cycle.id, str(cycle))
                for cycle in (
                    db.session.execute(select(Cycle).order_by(Cycle.created_at.desc()))
                    .scalars()
                    .all()
                )
            ]
        )
        self.cycle.choices = cycle_choices
