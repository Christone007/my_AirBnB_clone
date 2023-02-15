#!/usr/bin/python3
"""Defines all common attributes and methods for
all other classes"""

import uuid
import datetime
from models import storage


class BaseModel:
    """The Base class for all models"""

    def __init__(self, *arg, **kwargs):
        """Initialize a BaseModel object"""

        if kwargs is not None and len(kwargs) > 0:
            for k, v in kwargs.items():
                if k != "__class__":
                    self.__dict__[k] = v

            if 'created_at' in kwargs:
                self.created_at = datetime.datetime.fromisoformat(kwargs['created_at'])
            if 'updated_at' in kwargs:
                self.updated_at = datetime.datetime.fromisoformat(kwargs['updated_at'])

            self.name = type(self).__name__
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
        the current datetime and save"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation of an object"""

        my_dict = self.__dict__.copy()
        my_dict["__class__"] = self.__class__.__name__
        my_dict["created_at"] = my_dict["created_at"].isoformat()
        my_dict["updated_at"] = my_dict["updated_at"].isoformat()

        return my_dict
