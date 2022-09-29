"""
This file contains a script to populate the database.
"""

import os

from factories import UserFactory

first_name = os.environ["FIRST_NAME"]
first_surname = os.environ["FIRST_SURNAME"]
UserFactory(
    first_name=first_name, first_surname=first_surname, email="admin@example.com"
)
