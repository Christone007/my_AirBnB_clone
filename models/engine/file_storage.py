#!/usr/bin/python3
"""This module defines a FILE STORAGE system"""

import json


class FileStorage:
    """A Class to store serialize data into Files"""

    __file_path = ""
    __objects = {}

    def all(self):
        """Returns a dictionary of all objects available"""
        return __objects

    def new(self, obj):
        """Sets a new object with the correct key"""
        self.__objects[obj.name + '.' + obj.id] = obj.id
        
    def save(self):
        """Serializes objects to the JSON file"""
        obj_dict = self.__dict__.copy()

        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """deserializes the JSON file to a dictionary of objects"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                self.__objects = json.load(f)
        except Exception:
            pass
