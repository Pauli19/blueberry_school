"""This module is used to define fixtures."""

import pytest
from flask import Flask

from app import create_app, db


@pytest.fixture
def app() -> Flask:
    """Return a Flask app instance."""
    _app = create_app()
    with _app.app_context():
        db.create_all()
        yield _app
        db.session.remove()
        db.drop_all()
