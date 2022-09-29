"""
In this module, a Flask app is created using a factory function.
In addition, a shell context processor is implemented.
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
