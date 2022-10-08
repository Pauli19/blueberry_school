"""This module defines configuration classes for a Flask app."""

import os

DEBUG = os.getenv("FLASK_DEBUG") == "1"
TESTING = os.getenv("TESTING") == "1"
LOCAL_TEST = TESTING and DEBUG
ENABLED_FOR_DEV = DEBUG and not TESTING
DB_URI = os.environ["SQLALCHEMY_DATABASE_URI"]


class Config:  # pylint: disable=too-few-public-methods
    """This class represents a basic configuration for a Flask app."""

    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = f"{DB_URI}_test" if LOCAL_TEST else DB_URI
    SQLALCHEMY_ECHO = not TESTING
    SQLALCHEMY_RECORD_QUERIES = ENABLED_FOR_DEV
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = TESTING
    WTF_CSRF_ENABLED = not TESTING
    DEBUG_TB_INTERCEPT_REDIRECTS = False
