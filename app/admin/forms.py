"""This module contains forms for `admin` blueprint."""

from flask_wtf import FlaskForm
from sqlalchemy import select
from wtforms import (
    DateField,
    DateTimeField,
    EmailField,
    IntegerField,
    SelectField,
    StringField,
    SubmitField,
    TelField,
)
from wtforms.validators import Email, InputRequired, NumberRange

from .. import db
from ..models import Class, Level, Mode, Month, Representative, Sex, SubLevel


class RepresentativeForm(FlaskForm):
    """This class represents a form to create a representative."""

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
    submit = SubmitField("Create")


class StudentForm(FlaskForm):
    """This class represents a form to create a student."""

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
    birth_date = DateField("Birth Date", validators=[InputRequired()])
    email = EmailField("Email", validators=[Email()])
    phone_number = TelField("Phone Number", validators=[InputRequired()])
    representative = SelectField("Representative")
    class_ = SelectField("Class")
    submit = SubmitField("Create")

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
    )
    start_at = DateTimeField("Start At", validators=[InputRequired()])
    end_at = DateTimeField("End At", validators=[InputRequired()])
    level = SelectField(
        "Level",
        choices=[
            ("", "---"),
            (Level.L1.name, Level.L1.value),
            (Level.L2.name, Level.L2.value),
            (Level.L3.name, Level.L3.value),
        ],
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
    )
    submit = SubmitField("Create")
