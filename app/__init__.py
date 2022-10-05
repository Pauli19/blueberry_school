"""
This package contains the implementation of a factory
function to create and configure a Flask app.
"""

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from config import Config

# pylint: disable=fixme

bootstrap = Bootstrap5()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = "auth.login_get"
migrate = Migrate()


def create_app() -> Flask:
    """Create and configure a Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # TODO: improve extension initialization
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # TODO: improve blueprint registration
    from .auth import auth as auth_blueprint  # pylint: disable=import-outside-toplevel
    from .main import main as main_blueprint  # pylint: disable=import-outside-toplevel

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    return app
