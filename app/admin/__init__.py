"""
This package contains view functions associated with `admin` blueprint.
"""

# pylint: disable=cyclic-import

from flask import Blueprint

admin = Blueprint("admin", __name__)

from . import views  # pylint: disable=wrong-import-position
