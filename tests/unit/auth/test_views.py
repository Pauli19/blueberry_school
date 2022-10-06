"""This file contains tests for the view functions of `auth` blueprint."""

from flask import url_for
from flask.testing import FlaskClient
from flask_login import login_user

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


def test_anonymous_user_log_out(client: FlaskClient):
    """
    GIVEN an anonymous user
    WHEN user tries to logout
    THEN redirection to login_get view occurs
    """
    url = url_for("auth.logout")
    response = client.get(url, follow_redirects=True)

    assert response.status_code == 200
    assert response.request.path == url_for("auth.login_get")


def test_logged_in_user_logs_out(client: FlaskClient):
    """
    GIVEN a user that is logged in
    WHEN user tries to logout
    THEN user is logged out and redirected to main.index view
    """
    user = UserFactory()
    login_user(user)

    logout_url = url_for("auth.logout")
    response = client.get(logout_url, follow_redirects=True)

    assert response.status_code == 200
    assert response.request.path == url_for("main.index")
