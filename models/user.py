#!/usr/bin/python3
"""A module that defines a User"""

from models.base_model import BaseModel


class User(BaseModel):
    """A class that defines a User, inherits
    from BaseModel"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
