"""This module is used to define fixtures."""

import pytest
from flask import Flask

from app import create_app


@pytest.fixture
def app() -> Flask:
    """Return a Flask app instance."""
    return create_app()
