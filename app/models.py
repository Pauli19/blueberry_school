"""This module contains models and database utilities."""

from typing import Any

import sqlalchemy as sa
from flask_login import UserMixin
from sqlalchemy import select
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import composite
from sqlalchemy.sql.compiler import SQLCompiler
from sqlalchemy.sql.expression import FunctionElement
from sqlalchemy_utils import EmailType, PhoneNumber
from werkzeug.security import check_password_hash, generate_password_hash

from . import db, login_manager


class utc_now(FunctionElement):  # pylint: disable=invalid-name,too-many-ancestors
    """This class is used to define a DateTime column which timezone is UTC."""

    type = sa.DateTime()
    inherit_cache = True


@compiles(utc_now, "postgresql")
def pg_utc_now(
    element: utc_now,  # pylint: disable=unused-argument
    compiler: SQLCompiler,  # pylint: disable=unused-argument
    **kwargs: Any,  # pylint: disable=unused-argument
) -> str:
    """Return a string representing the current timestamp in UTC."""
    return "TIMEZONE('utc', CURRENT_TIMESTAMP)"


class BaseModel(db.Model):  # pylint: disable=too-few-public-methods
    """This class represents a base abstract model."""

    __abstract__ = True
    created_at = sa.Column(sa.DateTime, default=utc_now(), nullable=False)
    updated_at = sa.Column(
        sa.DateTime, default=utc_now(), onupdate=utc_now(), nullable=False
    )


class User(UserMixin, BaseModel):  # pylint: disable=too-few-public-methods
    """This class is used to model users."""

    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Unicode(255), nullable=False)
    second_name = sa.Column(sa.Unicode(255))
    first_surname = sa.Column(sa.Unicode(255), nullable=False)
    second_surname = sa.Column(sa.Unicode(255))
    email = sa.Column(EmailType, unique=True, nullable=False)
    password_hash = sa.Column(sa.Unicode(255))

    def __str__(self) -> str:
        return f"{self.first_name} {self.first_surname} - {self.email}"

    def __repr__(self) -> str:
        return (
            f'User(first_name="{self.first_name}", '
            f'first_surname="{self.first_surname}", '
            f'email="{self.email}")'
        )

    @property
    def full_name(self) -> str:
        """User's full name."""
        names = [
            self.first_name,
            self.second_name,
            self.first_surname,
            self.second_surname,
        ]
        return " ".join(name for name in names if name is not None)

    @property
    def password(self) -> str:
        """User's password."""
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password: str) -> None:
        """Hash User's password and set User's password_hash."""
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        """Verify User's password"""
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id: str) -> User | None:
    """Retrieve a User instance whose id is user_id."""
    return db.session.execute(
        select(User).where(User.id == user_id)
    ).scalar_one_or_none()


class Student(BaseModel):  # pylint: disable=too-few-public-methods
    """This class is used to model students."""

    id = sa.Column(sa.Integer, primary_key=True)
    identity_document = sa.Column(sa.Unicode(255), unique=True, nullable=False)
    first_name = sa.Column(sa.Unicode(255), nullable=False)
    second_name = sa.Column(sa.Unicode(255))
    first_surname = sa.Column(sa.Unicode(255), nullable=False)
    second_surname = sa.Column(sa.Unicode(255))
    email = sa.Column(EmailType, unique=True, nullable=False)
    birth_date = sa.Column(sa.Date, nullable=False)
    _phone_number = sa.Column(sa.Unicode(255))
    phone_country_code = sa.Column(sa.Unicode(8))
    phone_number = composite(PhoneNumber, _phone_number, phone_country_code)
