"""This module contains forms for `auth` blueprint."""

from flask_wtf import FlaskForm
from wtforms import BooleanField, EmailField, PasswordField, SubmitField
from wtforms.validators import Email, InputRequired


class LoginForm(FlaskForm):
    """This class represents a form to login."""

    email = EmailField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    remember_me = BooleanField("Remember me?")
    submit = SubmitField("Log In")
