"""This module contains forms for `admin` blueprint."""

from flask_wtf import FlaskForm
from sqlalchemy import select
from wtforms import (
    DateField,
    EmailField,
    SelectField,
    StringField,
    SubmitField,
    TelField,
)
from wtforms.validators import Email, InputRequired

from .. import db
from ..models import Class, Representative, Sex


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
        self.representative.choices = [("", "No representative")]
        representative_choices = [
            (representative.id, str(representative))
            for representative in (
                db.session.execute(
                    select(Representative).order_by(Representative.created_at.desc())
                )
                .scalars()
                .all()
            )
        ]
        self.representative.choices.extend(representative_choices)

        self.class_.choices = [("", "No class")]
        class_choices = [
            (class_.id, str(class_))
            for class_ in (
                db.session.execute(select(Class).order_by(Class.created_at.desc()))
                .scalars()
                .all()
            )
        ]
        self.class_.choices.extend(class_choices)
