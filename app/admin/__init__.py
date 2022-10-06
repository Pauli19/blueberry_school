"""
This package contains view functions associated to `admin` blueprint.
"""

# pylint: disable=cyclic-import

from flask import Blueprint

admin = Blueprint("admin", __name__)

from . import views  # pylint: disable=wrong-import-position
