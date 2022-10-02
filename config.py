"""This module defines configuration classes for a Flask app."""

import os

DEBUG = os.getenv("FLASK_DEBUG") == "1"
TESTING = os.getenv("TESTING") == "1"
LOCAL_TEST = TESTING and DEBUG
DB_URI = os.environ["SQLALCHEMY_DATABASE_URI"]


class Config:  # pylint: disable=too-few-public-methods
    """This class represents a basic configuration for a Flask app."""

    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = f"{DB_URI}_test" if LOCAL_TEST else DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = TESTING


print("=" * 50)
print(f"{DEBUG=}")
print(f"{TESTING=}")
print(f"{Config.SQLALCHEMY_DATABASE_URI}")
print("=" * 50)
