"""This module defines configuration classes for a Flask app."""

import os


class Config:  # pylint: disable=too-few-public-methods
    """This class represents a basic configuration for a Flask app."""

    SECRET_KEY = os.environ["SECRET_KEY"]
    SQLALCHEMY_DATABASE_URI = os.environ["SQLALCHEMY_DATABASE_URI"]
    SQLALCHEMY_TRACK_MODIFICATIONS = False
