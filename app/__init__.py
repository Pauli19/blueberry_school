"""
This package contains the implementation of a factory
function to create and configure a Flask app.
"""

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

from config import ENABLED_FOR_DEV, Config

# pylint: disable=fixme,import-outside-toplevel

bootstrap = Bootstrap5()
db = SQLAlchemy(
    metadata=MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )
)
login_manager = LoginManager()
login_manager.login_view = "auth.login_get"
migrate = Migrate()

if ENABLED_FOR_DEV:
    from flask_debugtoolbar import DebugToolbarExtension

    toolbar = DebugToolbarExtension()


def create_app() -> Flask:
    """Create and configure a Flask application."""
    app = Flask(__name__)
    app.config.from_object(Config)

    # TODO: improve extension initialization
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    if ENABLED_FOR_DEV:
        toolbar.init_app(app)

    # TODO: improve blueprint registration
    from .admin import admin as admin_blueprint
    from .auth import auth as auth_blueprint
    from .main import main as main_blueprint

    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix="/auth")
    app.register_blueprint(admin_blueprint, url_prefix="/admin")

    return app
