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

# pylint: disable=fixme,import-outside-toplevel

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
    from .admin import admin as admin_blueprint
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(admin_blueprint, url_prefix="/admin")

    return app
