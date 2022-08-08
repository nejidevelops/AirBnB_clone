#!/usr/bin/python3
"""Def the City class."""
from models.base_model import BaseModel


class City(BaseModel):

    """Represent a city class.

    Attributes:
        state_id (str): The state id.
        name (str): The name of the city.
    """

    state_id = ""
    name = ""
