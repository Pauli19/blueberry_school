"""This module contains tests for models."""
import datetime

import pytest

from app.models import Representative, Student, User, load_user
from factories import RepresentativeFactory, StudentFactory, UserFactory


def test_user_creation(app):  # pylint: disable=unused-argument
    """
    GIVEN
        first_name is "John"
        first_surname is "Smith" and
        email is "user@example.com"
    WHEN a User instance is created
    THEN User is created properly
        - data is stored in the database
        - information is set properly
    """
    first_name = "John"
    first_surname = "Smith"
    email = "user@example.com"
    user = UserFactory(first_name=first_name, first_surname=first_surname, email=email)

    assert user.id is not None
    assert user.first_name == first_name
    assert user.first_surname == first_surname
    assert user.email == email


def test_user_str():
    """
    GIVEN a User instance which
        first_name is "John"
        first_surname is "Smith" and
        email is "user@example.com"
    WHEN converted to a string
    THEN the string is
        "John Smith - user@example.com"
    """
    user = User(first_name="John", first_surname="Smith", email="user@example.com")
    assert str(user) == "John Smith - user@example.com"


def test_user_representation():
    """
    GIVEN
        first_name is "John"
        first_surname is "Smith" and
        email is "user@example.com"
    WHEN calling repr
    THEN the returned string is
        'User(first_name="John", first_surname="Smith", email="user@example.com")'
    """
    user = User(first_name="John", first_surname="Smith", email="user@example.com")
    expected_repr = (
        'User(first_name="John", first_surname="Smith", email="user@example.com")'
    )
    assert repr(user) == expected_repr


@pytest.mark.parametrize(
    "user,expected_full_name",
    [
        pytest.param(
            User(
                first_name="John",
                second_name="James",
                first_surname="Smith",
                second_surname="Black",
            ),
            "John James Smith Black",
            id="all-names",
        ),
        pytest.param(
            User(
                first_name="John",
                second_name="James",
                first_surname="Smith",
            ),
            "John James Smith",
            id="two-names-first-surname",
        ),
        pytest.param(
            User(
                first_name="John",
                first_surname="Smith",
                second_surname="Black",
            ),
            "John Smith Black",
            id="first-name-two-surnames",
        ),
        pytest.param(
            User(first_name="John", first_surname="Smith"),
            "John Smith",
            id="first-name-first-surname",
        ),
    ],
)
def test_user_full_name(user, expected_full_name):
    """
    GIVEN a User instance
    WHEN getting its property full_name
    THEN property is equal to expected_full_name
    """
    assert user.full_name == expected_full_name


def test_user_password_not_readable():
    """
    GIVEN a User instance which
        first_name is "John"
        last_name is "Smith"
        and email is "user@example.com"
    WHEN trying to access password
    THEN verify that
        - an AttributeError exception is raised
        - exception message is "password is not a readable attribute"
    """
    user = User(first_name="John", first_surname="Smith", email="user@example.com")
    message = "password is not a readable attribute"
    with pytest.raises(AttributeError, match=message):
        user.password  # pylint: disable=pointless-statement


def test_user_password_is_hashed():
    """
    GIVEN a User instance
    WHEN user's password is set
    THEN user's password_hash is not None
    """
    user = User()
    user.password = "this-is-a-password"
    assert user.password_hash is not None


def test_load_user(app):  # pylint: disable=unused-argument
    """
    GIVEN a User instance
    WHEN calling load_user with User instance's id
    THEN User instance is the same as loaded User instance
    """
    first_name = "John"
    first_surname = "Smith"
    email = "user@example.com"
    user = UserFactory(first_name=first_name, first_surname=first_surname, email=email)
    loaded_user = load_user(user.id)

    assert user == loaded_user


def test_user_verify_password():
    """
    GIVEN a User instance with password
    WHEN verifying password
    THEN User's verify_password method returns
        - True when the password is verified
        - False when the password is not verified
    """
    password = "this-is-a-password"
    user = User(password=password)

    assert user.verify_password(password)
    assert not user.verify_password("this-is-another-password")


def test_student_creation(app):  # pylint: disable=unused-argument
    """
    GIVEN
        identity_document is "1020304050"
        first_name is "Ben"
        first_surname is "Hazlewood"
        email is "benhazlewood@example.com"
        birth_date is "1995-01-01"
    WHEN a Student instance is created
    THEN Student is created properly
        - data is stored in the database
        - information is set properly
    """
    identity_document = "1020304050"
    first_name = "Ben"
    first_surname = "Hazlewood"
    email = "benhazlewood@example.com"
    birth_date = datetime.date(1995, 1, 1)
    student = StudentFactory(
        identity_document=identity_document,
        first_name=first_name,
        first_surname=first_surname,
        email=email,
        birth_date=birth_date,
    )

    assert student.id is not None
    assert student.identity_document == identity_document
    assert student.first_name == first_name
    assert student.first_surname == first_surname
    assert student.email == email
    assert student.birth_date == birth_date


def test_student_creation_with_representative(app):  # pylint: disable=unused-argument
    """
    GIVEN
        identity_document is "1020304050"
        first_name is "Ben"
        first_surname is "Hazlewood"
        email is "benhazlewood@example.com"
        birth_date is "1995-01-01"
        and an associated representative
    WHEN a Student instance is created
    THEN Student is created properly
        - data is stored in the databse
        - information is set properly
    """
    identity_document = "1020304050"
    first_name = "Ben"
    first_surname = "Hazlewood"
    email = "benhazlewood@example.com"
    birth_date = datetime.date(1995, 1, 1)
    representative = RepresentativeFactory()
    student: Student = Student(
        identity_document=identity_document,
        first_name=first_name,
        first_surname=first_surname,
        email=email,
        birth_date=birth_date,
        representative=representative,
    )

    assert student.id is not None
    assert student.identity_document == identity_document
    assert student.first_name == first_name
    assert student.first_surname == first_surname
    assert student.email == email
    assert student.birth_date == birth_date
    assert student.representative == representative


def test_student_str():
    """
    GIVEN a Student instance which
        identity_document is "1020304050"
        first_name is "Ben"
        first_surname is "Hazlewood"
    WHEN converted to a string
    THEN the string is
        "1020304050 - Ben Hazlewood"
    """
    student = Student(
        identity_document="1020304050",
        first_name="Ben",
        first_surname="Hazlewood",
    )
    assert str(student) == "1020304050 - Ben Hazlewood"


def test_student_representation():
    """
    GIVEN a Student instance which
        identity_document is "1020304050"
        first_name is "Ben"
        first_surname is "Hazlewood"
    WHEN calling repr
    THEN the returned string is
        'Student(
            identity_document="1020304050",
            first_name="Ben",
            first_surname="Hazlewood")'
    """
    student = Student(
        identity_document="1020304050",
        first_name="Ben",
        first_surname="Hazlewood",
    )
    expected_repr = (
        'Student(identity_document="1020304050", '
        'first_name="Ben", first_surname="Hazlewood")'
    )
    assert repr(student) == expected_repr


def test_representative_creation(app):  # pylint: disable=unused-argument
    """
    GIVEN
        identity_document is "1020304050"
        first_name is "Katy"
        first_surname is "Perry"
        phone_number is "+593987654321"
    WHEN a Representative instance is created
    THEN Representative is created properly
        - data is stored in the database
        - information is set properly
    """
    identity_document = "1020304050"
    first_name = "Katy"
    first_surname = "Perry"
    phone_number = "+593987654321"
    representative = RepresentativeFactory(
        identity_document=identity_document,
        first_name=first_name,
        first_surname=first_surname,
        phone_number=phone_number,
    )

    assert representative.id is not None
    assert representative.identity_document == identity_document
    assert representative.first_name == first_name
    assert representative.first_surname == first_surname
    assert representative.phone_number.e164 == phone_number


def test_representative_str():
    """
    GIVEN a Representative instance which
        identity_document is "1020304050"
        first_name is "Katy"
        first_surname is "Perry"
    WHEN when converted to a string
    THEN the string is
        "1020304050 - Katy Perry"
    """
    representative = Representative(
        identity_document="1020304050",
        first_name="Katy",
        first_surname="Perry",
    )
    assert str(representative) == "1020304050 - Katy Perry"


def test_representative_representation():
    """
    GIVEN a Representative instance which
        identity_document is "1020304050"
        first_name is "Katy"
        first_surname is "Perry"
    WHEN calling repr
    THEN the returned string is
        'Representative(
            identity_document="1020304050"
            first_name="Katy",
            first_surname="Perry")'
    """
    representative = Representative(
        identity_document="1020304050", first_name="Katy", first_surname="Perry"
    )
    expected_repr = (
        'Representative(identity_document="1020304050", '
        'first_name="Katy", first_surname="Perry")'
    )
    assert repr(representative) == expected_repr
