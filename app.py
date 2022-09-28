"""
This module contains logic for the creation and configuration
of the Flask app. In addition, it contains the view functions
associated with the app, 404, and 500 view functions.
"""

import os
from typing import Any

import sqlalchemy as sa
from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import EmailType
from werkzeug.exceptions import InternalServerError, NotFound

app = Flask(__name__)
app.secret_key = os.environ["SECRET_KEY"]
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap5(app)


# Models
class User(db.Model):  # pylint: disable=too-few-public-methods
    """This class is used to model users."""

    id = sa.Column(sa.Integer, primary_key=True)
    first_name = sa.Column(sa.Unicode(255), nullable=False)
    second_name = sa.Column(sa.Unicode(255))
    first_surname = sa.Column(sa.Unicode(255), nullable=False)
    second_surname = sa.Column(sa.Unicode(255))
    email = sa.Column(EmailType, unique=True, nullable=False)


# Shell Context Processor
@app.shell_context_processor
def make_shell_context() -> dict[str, Any]:
    """Load items into the shell."""
    return dict(db=db, User=User)


# View Functions
@app.get("/")
def index() -> str:
    """View function for "/" route."""
    return render_template("index.html.jinja")


@app.errorhandler(404)
def page_not_found(exc: NotFound) -> tuple[str, int]:  # pylint: disable=unused-argument
    """Error handler for 404 status code."""
    return render_template("404.html.jinja"), 404


@app.errorhandler(500)
def internal_server_error(
    exc: InternalServerError,  # pylint: disable=unused-argument
) -> tuple[str, int]:
    """Error handler for 500 status code."""
    return render_template("500.html.jinja"), 500
