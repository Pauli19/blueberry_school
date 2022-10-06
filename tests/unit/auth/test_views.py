"""This file contains tests for views of `auth` blueprint."""

from flask import url_for
from flask.testing import FlaskClient

from app.auth.forms import LoginForm
from factories import UserFactory


def test_email_no_user_cannot_login(client: FlaskClient):
    """
    GIVEN an email that is not associated with a user
    WHEN trying to login
    THEN redirection to login page occurs
    """
    url = url_for("auth.login_post")
    form = LoginForm(email="fake-user@example.com", password="pass123")
    response = client.post(url, data=form.data, follow_redirects=True)

    assert response.status_code == 200
    assert response.request.path == url_for("auth.login_get")


def test_user_without_password_cannot_login(client: FlaskClient):
    """
    GIVEN a user that exists in the database without a password
    WHEN trying to login
    THEN redirection to login page occurs
    """
    user = UserFactory()
    url = url_for("auth.login_post")
    form = LoginForm(email=user.email, password="pass123")
    response = client.post(url, data=form.data, follow_redirects=True)

    assert response.status_code == 200
    assert response.request.path == url_for("auth.login_get")


def test_user_with_wrong_credentials_cannot_login(client: FlaskClient):
    """
    GIVEN a user that exists in the database
    WHEN trying to login with wrong credentials
    THEN redirection to login page occurs
    """
    user = UserFactory(password="pass123")
    url = url_for("auth.login_post")
    form = LoginForm(email=user.email, password="wrong-pass")
    response = client.post(url, data=form.data, follow_redirects=True)

    assert response.status_code == 200
    assert response.request.path == url_for("auth.login_get")


def test_user_with_right_credentials_is_logged_in(client: FlaskClient):
    """
    GIVEN a user that exists in the database
    WHEN trying to login with correct credentials
    THEN login is completed successfully
    """
    password = "pass123"
    user = UserFactory(password=password)
    url = url_for("auth.login_post")
    form = LoginForm(email=user.email, password=password)
    response = client.post(url, data=form.data, follow_redirects=True)

    assert response.status_code == 200
    assert response.request.path == url_for("admin.index")
