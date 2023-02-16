#!/usr/bin/python3
"""A module for Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Defines Review Objects"""
    place_id = ''
    user_id = ''
    text = ''
