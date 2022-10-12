"""
In this module, a Flask app is created using a factory function.
In addition, a shell context processor is implemented.
"""

from typing import Any

from app import create_app, db
from app.models import models
from factories import factories

app = create_app()


# Shell Context Processor
@app.shell_context_processor
def make_shell_context() -> dict[str, Any]:
    """Load items into the shell."""
    factory_dict = {cls.__name__: cls for cls in factories}
    model_dict = {cls.__name__: cls for cls in models}
    return factory_dict | model_dict | dict(db=db, session=db.session)
