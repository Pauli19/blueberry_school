"""
This module is the starting point for this Flask app.
It creates a Flask app using a factory function. In addition,
it implements a shell context processor.
"""

from typing import Any

from app import create_app, db
from app.models import User

app = create_app()


# Shell Context Processor
@app.shell_context_processor
def make_shell_context() -> dict[str, Any]:
    """Load items into the shell."""
    return dict(db=db, session=db.session, User=User)
