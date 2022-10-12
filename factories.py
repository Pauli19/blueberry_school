"""This module contains factories to facilitate creating model instances."""

import datetime

from factory import Faker, LazyAttribute, fuzzy
from factory.alchemy import SQLAlchemyModelFactory

from app.models import Student, User, db


class UserFactory(SQLAlchemyModelFactory):
    """This is a factory to create User instances."""

    class Meta:  # pylint: disable=missing-class-docstring,too-few-public-methods
        model = User
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    first_name = Faker("first_name")
    first_surname = Faker("last_name")
    email = LazyAttribute(lambda o: f"{o.first_name}{o.first_surname}@example.com")


class StudentFactory(SQLAlchemyModelFactory):
    """This is a factory to create Student instances."""

    class Meta:  # pylint: disable=missing-class-docstring,too-few-public-methods
        model = Student
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    identity_document = fuzzy.FuzzyText(length=10, prefix="1", chars="1234567890")
    first_name = Faker("first_name")
    first_surname = Faker("last_name")
    email = LazyAttribute(lambda o: f"{o.first_name}{o.first_surname}@example.com")
    birth_date = fuzzy.FuzzyDate(
        start_date=datetime.date(1980, 1, 1), end_date=datetime.date(2012, 1, 1)
    )


factories = [UserFactory, StudentFactory]
