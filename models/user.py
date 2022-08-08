#!/usr/bin/python3

"""Defines the User class."""

from models.base_model import BaseModel


class User(BaseModel):

    """Represent a User.

    Attributes:
        email: Email of the user.
        password: Password of the user.
        first_name: The first name of the user.
        last_name: The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
