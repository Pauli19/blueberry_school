"""
This package contains the implementation of the factory
function to create and configure the Flask app.
"""
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

bootstrap = Bootstrap5()
db = SQLAlchemy()
migrate = Migrate()


def create_app() -> Flask:
    """Create and configure a Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)

    bootstrap.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)

    from .main import main as main_blueprint  # pylint: disable=import-outside-toplevel

    app.register_blueprint(main_blueprint)

    return app
