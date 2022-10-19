"""This module contains forms for `admin` blueprint."""

from flask_wtf import FlaskForm
from wtforms import EmailField, SelectField, StringField, SubmitField, TelField
from wtforms.validators import Email, InputRequired, Length

from ..models import Sex


class RepresentativeForm(FlaskForm):
    """This class represents a form to create a representative."""

    identity_document = StringField(
        "Identity Document", validators=[InputRequired(), Length(min=10, max=10)]
    )
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
