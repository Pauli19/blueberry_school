"""This module contains tests for models."""
import pytest

from app.models import User
from factories import UserFactory


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
    WHEN converted to string
    THEN string is
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
