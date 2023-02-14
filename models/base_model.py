#!/usr/bin/python3
"""Defines all common attributes and methods for
all other classes"""

import uuid
import datetime
from __init__ import storage


class BaseModel:
    """The Base class for all models"""

    def __init__(self, *arg, **kwargs):
        """Initialize a BaseModel object"""

        if kwargs is not None and len(kwargs) > 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'created_at' in kwargs:
                self.created_at = datetime.datetime.fromisoformat(kwargs['created_at'])
            if 'updated_at' in kwargs:
                self.updated_at = datetime.datetime.fromisoformat(kwargs['updated_at'])
            if 'my_number' in kwargs:
                self.my_number = kwargs['my_number']
            if 'name' in kwargs:
                self.name = kwargs['name']
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)


    def __str__(self):
        """Prints a string representation of the instance"""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
            self.id, self.__dict__))

    def save(self):
        """Updates the public instance attribute `updated_at` with
        the current datetime"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an object"""
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()

        obj_dict = self.__dict__
        obj_dict["__class__"] =  self.__class__.__name__

        return obj_dict
