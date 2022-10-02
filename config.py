"""This module defines configuration classes for a Flask app."""

import os

DEBUG = os.getenv("FLASK_DEBUG") == "1"
TEST_MODE = os.getenv("TEST_MODE") == "true"
DB_URI = os.environ["SQLALCHEMY_DATABASE_URI"]


class Config:  # pylint: disable=too-few-public-methods
    """This class represents a basic configuration for a Flask app."""

    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = f"{DB_URI}_test" if TEST_MODE else DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = DEBUG or TEST_MODE
