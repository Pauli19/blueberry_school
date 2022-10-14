"""This module contains models and database utilities."""

from enum import Enum
from typing import Any

import sqlalchemy as sa
from flask_login import UserMixin
from sqlalchemy import select
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm import relationship
from sqlalchemy.sql.compiler import SQLCompiler
from sqlalchemy.sql.expression import FunctionElement
from sqlalchemy_utils import EmailType, PhoneNumberType
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
    phone_number = sa.Column(PhoneNumberType())

    representative_id = sa.Column(sa.Integer, sa.ForeignKey("representative.id"))
    representative = relationship("Representative", back_populates="students")
    class_id = sa.Column(sa.Integer, sa.ForeignKey("class.id"))
    class_ = relationship("Class", back_populates="students")

    def __str__(self) -> str:
        return f"{self.identity_document} - {self.first_name} {self.first_surname}"

    def __repr__(self) -> str:
        return (
            f'Student(identity_document="{self.identity_document}", '
            f'first_name="{self.first_name}", '
            f'first_surname="{self.first_surname}")'
        )


class Representative(BaseModel):  # pylint: disable=too-few-public-methods
    """This class is used to model students' representatives."""

    id = sa.Column(sa.Integer, primary_key=True)
    identity_document = sa.Column(sa.Unicode(255), unique=True, nullable=False)
    first_name = sa.Column(sa.Unicode(255), nullable=False)
    second_name = sa.Column(sa.Unicode(255))
    first_surname = sa.Column(sa.Unicode(255), nullable=False)
    second_surname = sa.Column(sa.Unicode(255))
    email = sa.Column(EmailType, unique=True)
    phone_number = sa.Column(PhoneNumberType(), nullable=False)

    students = relationship("Student", back_populates="representative")

    def __str__(self) -> str:
        return f"{self.identity_document} - {self.first_name} {self.first_surname}"

    def __repr__(self) -> str:
        return (
            f'Representative(identity_document="{self.identity_document}", '
            f'first_name="{self.first_name}", '
            f'first_surname="{self.first_surname}")'
        )


class Month(str, Enum):  # pylint: disable=too-few-public-methods
    """This enumeration is used to represent months."""

    JANUARY = "January"
    FEBRUARY = "February"
    MARCH = "March"
    APRIL = "April"
    MAY = "May"
    JUNE = "June"
    JULY = "July"
    AUGUST = "August"
    SEPTEMBER = "September"
    OCTOBER = "October"
    NOVEMBER = "November"
    DECEMBER = "December"


class Cycle(BaseModel):  # pylint: disable=too-few-public-methods
    """This class is used to model cycles."""

    id = sa.Column(sa.Integer, primary_key=True)
    month = sa.Column(sa.Enum(Month), nullable=False)
    year = sa.Column(sa.Integer, nullable=False)
    start_date = sa.Column(sa.Date, nullable=False)
    end_date = sa.Column(sa.Date, nullable=False)

    classes = relationship("Class", back_populates="cycle")

    def __str__(self) -> str:
        return f"{self.month} - {self.year}"

    def __repr__(self) -> str:
        return f'Cycle(month="{self.month}", year={self.year})'


class Mode(str, Enum):  # pylint: disable=too-few-public-methods
    """This enumeration is used to represent class modes."""

    NORMAL = "Normal"
    INTENSIVE = "Intensive"


class Level(str, Enum):  # pylint: disable=too-few-public-methods
    """This enumeration is used to represent class levels."""

    L1 = "L1"
    L2 = "L2"
    L3 = "L3"


class SubLevel(str, Enum):  # pylint: disable=too-few-public-methods
    """This enumeration is used to represent class sub levels."""

    P1 = "P1"
    P2 = "P2"
    P3 = "P3"
    P4 = "P4"


class Class(BaseModel):  # pylint: disable=too-few-public-methods
    """This class is used to model classes."""

    id = sa.Column(sa.Integer, primary_key=True)
    mode = sa.Column(sa.Enum(Mode), nullable=False)
    start_at = sa.Column(sa.Time, nullable=False)
    end_at = sa.Column(sa.Time, nullable=False)
    level = sa.Column(sa.Enum(Level), nullable=False)
    sub_level = sa.Column(sa.Enum(SubLevel), nullable=False)

    cycle_id = sa.Column(sa.Integer, sa.ForeignKey("cycle.id"))
    cycle = relationship("Cycle", back_populates="classes")
    students = relationship("Student", back_populates="class")


models = [User, Student, Representative, Cycle, Class]
