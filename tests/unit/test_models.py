"""This module contains tests for models."""
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


def test_user_full_name_both_names_and_both_surnames():
    """
    GIVEN
        first_name is "John"
        second_name is "James"
        first_surname is "Smith" and
        second_surname is "Black"
    WHEN getting full_name
    THEN the returned string is
        "John James Smith Black"
    """
    user = User(
        first_name="John",
        second_name="James",
        first_surname="Smith",
        second_surname="Black",
    )
    assert user.full_name == "John James Smith Black"


def test_user_full_name_only_first_name_and_first_surname():
    """
    GIVEN
        first_name is "John" and
        first_surname is "Smith"
    WHEN getting full_name
    THEN the returned string is
        "John Smith"
    """
    user = User(first_name="John", first_surname="Smith")

    assert user.full_name == "John Smith"
