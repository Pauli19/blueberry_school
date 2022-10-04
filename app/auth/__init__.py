"""
This package contains view functions associated to `auth` blueprint.
"""

# pylint: disable=cyclic-import

from flask import Blueprint

auth = Blueprint("auth", __name__)

from . import views  # pylint: disable=wrong-import-position
