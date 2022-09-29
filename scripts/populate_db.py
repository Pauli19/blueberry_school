"""
This file contains a script to populate the database.
"""

from app.models import User, db

users = [
    User(
        first_name="Luis",
        second_name="Miguel",
        first_surname="Vargas",
        second_surname="Fonseca",
        email="lmiguelvargasf@gmail.com",
    ),
    User(
        first_name="Dora",
        second_name="Paulina",
        first_surname="Gaibor",
        second_surname="Llanos",
        email="dpgaibor@outlook.com",
    ),
]
session = db.session
session.add_all(users)  # pylint: disable=no-member
session.commit()  # pylint: disable=no-member
