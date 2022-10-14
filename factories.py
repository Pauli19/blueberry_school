"""This module contains factories to facilitate creating model instances."""

import datetime
import random

from factory import Faker, LazyAttribute, fuzzy, lazy_attribute
from factory.alchemy import SQLAlchemyModelFactory

from app.models import Cycle, Month, Representative, Student, User, db


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

    identity_document = fuzzy.FuzzyText(length=9, prefix="1", chars="1234567890")
    first_name = Faker("first_name")
    first_surname = Faker("last_name")
    email = LazyAttribute(lambda o: f"{o.first_name}{o.first_surname}@example.com")
    birth_date = fuzzy.FuzzyDate(
        start_date=datetime.date(1980, 1, 1), end_date=datetime.date(2012, 1, 1)
    )


class RepresentativeFactory(SQLAlchemyModelFactory):
    """This is a factory to create Representative instances."""

    class Meta:  # pylint: disable=missing-class-docstring,too-few-public-methods
        model = Representative
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    identity_document = fuzzy.FuzzyText(length=9, prefix="1", chars="1234567890")
    first_name = Faker("first_name")
    first_surname = Faker("last_name")
    phone_number = fuzzy.FuzzyText(length=8, prefix="+5939", chars="1234567890")


class CycleFactory(SQLAlchemyModelFactory):
    """This is a factory to create Cycle instances"""

    class Meta:  # pylint: disable=missing-class-docstring,too-few-public-methods
        model = Cycle
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    month = fuzzy.FuzzyChoice(choices=list(Month))
    year = fuzzy.FuzzyInteger(low=2022, high=2050)
    start_date = fuzzy.FuzzyDate(
        start_date=datetime.date(2022, 11, 1), end_date=datetime.date(2050, 12, 31)
    )

    @lazy_attribute
    def end_date(self) -> datetime.date:
        """
        Cycle's end_date. This value is greater than Cycle's start_date.
        There is a difference of 28 to 31 days, randomly picked, between
        end_date and start_date.
        """
        delta_days = random.randrange(28, 31)
        return self.start_date + datetime.timedelta(days=delta_days)


factories = [UserFactory, StudentFactory, RepresentativeFactory, CycleFactory]
