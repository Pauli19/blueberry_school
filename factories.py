"""This module contains factories to facilitate creating model instances."""

from factory import Faker
from factory.alchemy import SQLAlchemyModelFactory

from app.models import User, db


class UserFactory(SQLAlchemyModelFactory):
    """This is a factory to create User instances."""

    class Meta:  # pylint: disable=missing-class-docstring,too-few-public-methods
        model = User
        sqlalchemy_session = db.session

    first_name = Faker("first_name")
    first_surname = Faker("last_name")
    email = Faker("email")
