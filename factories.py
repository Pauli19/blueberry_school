"""This module contains factories to facilitate creating model instances."""

import datetime
import random

from factory import Faker, LazyAttribute, SubFactory, fuzzy, lazy_attribute
from factory.alchemy import SQLAlchemyModelFactory

from app.models import (
    Class,
    Cycle,
    Level,
    Mode,
    Month,
    Representative,
    Student,
    SubLevel,
    User,
    db,
)


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

    @lazy_attribute
    def start_date(self) -> datetime.date:
        """
        Cycle's start_date. This value is generated based on Cycle's
        month and year. The date's day corresponds to the first day of
        the randomly generated month.
        """
        month = list(Month).index(self.month) + 1
        return datetime.datetime(self.year, month, 1)

    @lazy_attribute
    def end_date(self) -> datetime.date:
        """
        Cycle's end_date. This value generated based on Cycle's start_date.
        There is a difference of 25 to 30 days, randomly picked, between
        end_date and start_date.
        """
        delta_days = random.randrange(25, 31)
        return self.start_date + datetime.timedelta(days=delta_days)


class ClassFactory(SQLAlchemyModelFactory):
    """This is a factory to create Classes Instances."""

    class Meta:  # pylint: disable=missing-class-docstring,too-few-public-methods
        model = Class
        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = "commit"

    mode = fuzzy.FuzzyChoice(choices=list(Mode))
    level = fuzzy.FuzzyChoice(choices=list(Level))
    sub_level = fuzzy.FuzzyChoice(choices=list(SubLevel))
    cycle = SubFactory(CycleFactory)

    @lazy_attribute
    def start_at(self) -> datetime.time:
        """
        Class' start_at. This value is randomly generated.
        The hour's minutes corresponds to zero because a
        class must start at an o'clock time.
        """
        hour = random.randrange(17, 21)
        return datetime.time(hour)

    @lazy_attribute
    def end_at(self) -> datetime.time:
        """
        Class' end_at. This value is generated based on Class' start_at.
        There is a difference of one hour between end_at and start_at.
        """
        start = datetime.datetime(
            2000,
            1,
            1,
            hour=self.start_at.hour,
            minute=self.start_at.minute,
            second=self.start_at.second,
        )
        end = start + datetime.timedelta(hours=1)
        return end.time()


factories = [
    UserFactory,
    StudentFactory,
    RepresentativeFactory,
    CycleFactory,
    ClassFactory,
]
