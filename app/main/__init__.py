"""
This package contains error handlers and view functions associated
to the Blueprint `main`.
"""
# pylint: disable=cyclic-import

from flask import Blueprint

main = Blueprint("main", __name__)

from . import errors, views  # pylint: disable=wrong-import-position
