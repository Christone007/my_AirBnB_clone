#!/usr/bin/python3
"""This module defines a FILE STORAGE system"""

import json

class FileStorage:
    """A Class to store serialize data into Files"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns a dictionary of all objects available"""
        return self.__objects

    def new(self, obj):
        """Sets a new object with the correct key"""
        FileStorage.__objects[type(obj).__name__ + '.' + obj.id] = obj

    def save(self):
        """Serializes objects to the JSON file"""
        obj_dict = {k:v.to_dict() for k,v in FileStorage.__objects.items()}
        
        try:
            with open(self.__file_path, 'w', encoding="utf-8") as f:
                obj_json = json.dumps(obj_dict)
                f.write(obj_json)
        except Exception:
            pass

    def reload(self):
        """deserializes the JSON file to a dictionary of objects"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                obj_dicts = json.load(f)
                if len(obj_dicts) > 0:
                    for k, v in obj_dicts.items():
                        obj = self.classes()[v["__class__"]](**v)
                        FileStorage.__objects[k] = obj
        except Exception:
            pass

    def classes(self):
        """Returns a dictionary of valid classes and their references"""
        from models.base_model import BaseModel
        from models.user import User

        classes = {"BaseModel": BaseModel,
                   "User": User}
        return classes
