#!/usr/bin/python3
"""This file contain the class City"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel class
    """
    state_id = ""
    name = ""
