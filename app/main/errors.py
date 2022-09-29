"""This module contains error handlers for a Flask app."""

from flask import render_template
from werkzeug.exceptions import InternalServerError, NotFound

from . import main


@main.app_errorhandler(404)
def page_not_found(exc: NotFound) -> tuple[str, int]:  # pylint: disable=unused-argument
    """Error handler for 404 status code."""
    return render_template("404.html.jinja"), 404


@main.app_errorhandler(500)
def internal_server_error(
    exc: InternalServerError,  # pylint: disable=unused-argument
) -> tuple[str, int]:
    """Error handler for 500 status code."""
    return render_template("500.html.jinja"), 500
