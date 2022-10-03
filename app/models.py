"""This module contains models and database utilities."""

from typing import Any

import sqlalchemy as sa
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql.compiler import SQLCompiler
from sqlalchemy.sql.expression import FunctionElement
from sqlalchemy_utils import EmailType

from . import db


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


# Models
class User(BaseModel):  # pylint: disable=too-few-public-methods
    """This class is used to model users."""

    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Unicode(255), nullable=False)
    second_name = sa.Column(sa.Unicode(255))
    first_surname = sa.Column(sa.Unicode(255), nullable=False)
    second_surname = sa.Column(sa.Unicode(255))
    email = sa.Column(EmailType, unique=True, nullable=False)

    def __str__(self) -> str:
        return f"{self.first_name} {self.first_surname} - {self.email}"

    def __repr__(self) -> str:
        return (
            f'User(first_name="{self.first_name}", '
            f'first_surname="{self.first_surname}", '
            f'email="{self.email}")'
        )
