#!/usr/bin/python3
"""This module defines a Command Line Interpreter for the program"""

import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """The interpreter class which inherits from Cmd class"""

    def __init__(self):
        """Initialize an interpreter object"""
        self.prompt = "(hbnb) "
        self.use_rawinput = False
        super().__init__()

    def emptyline(self):
        """When empty line is passed, do nothing"""
        pass

    def do_EOF(self, line):
        """Exit the interpreter"""
        return True

    def do_quit(self, line):
        """Exit the interpreter"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel"""
        if len(line) == 0:
            print("** class name missing **")
        elif line == "BaseModel":
            newModel = BaseModel()
            newModel.save()
            print(newModel.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if line == '' or line is None:
            print("** class name missing **")
        else:
            line_arr = line.split()
            if len(line_arr) == 1:
                if line_arr[0] != "BaseModel":
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            elif len(line_arr) == 2:
                class_name = line_arr[0]
                id_string = line_arr[1]

                if class_name != "BaseModel":
                    print("** class doesn't exist **")
                else:
                    try:
                        obj_key = class_name + '.' + id_string
                        obj_value = storage.all()[obj_key]
                        print(obj_value)
                    except KeyError:
                        print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if line == '' or line is None:
            print("** class name missing **")
        else:
            line_arr = line.split()
            if len(line_arr) == 1:
                if line_arr[0] != "BaseModel":
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            elif len(line_arr) == 2:
                class_name = line_arr[0]
                id_string = line_arr[1]

                if class_name != "BaseModel":
                    print("** class doesn't exist **")
                else:
                    try:
                        obj_key = class_name + '.' + id_string
                        del storage.all()[obj_key]
                    except KeyError:
                        print("** no instance found **")

                    storage.save()

    def do_all(self, line):
        """Prints String representation of All Instances or
        of a named Class"""

        objs_list = []
        if line == '' or line is None:
            for k, v in storage.all().items():
                objs_list.append(str(v))

        else:
            line_arr = line.split()
            class_name = line_arr[0]

            for k, v in storage.all().items():
                if v.__class__.__name__ == class_name:
                    objs_list.append(str(v))

            if len(objs_list) == 0:
                print("** class doesn't exist **")
                return

        print(objs_list)
    
    def do_update(self, line):
        """Updates an Instance based on the classname and id"""
        if line == '' or line is None:
            print("** class name missing **")
        else:
            line_arr = line.split(' ', 3)
            if len(line_arr) == 1:
                if line_arr[0] != "BaseModel":
                    print("** class doesn't exist **")
                else:
                    print("** instance id missing **")
            elif len(line_arr) == 2:
                if line_arr[0] != "BaseModel":
                    print("** class doesn't exist **")
                else:
                    obj_key = line_arr[0] + '.' + line_arr[1]
                    if obj_key not in storage.all():
                        print("** no instance found **")
                    else:
                        print("** attribute name missing **")
            elif len(line_arr) == 3:
                if line_arr[0] != "BaseModel":
                    print("** class doesn't exist **")
                else:
                    obj_key = line_arr[0] + '.' + line_arr[1]
                    if obj_key not in storage.all():
                        print("** no instance found **")
                    else:
                        print("** value missing **")
            else:
                class_name = line_arr[0]
                id_string = line_arr[1]
                attr_name = line_arr[2]
                attr_value = line_arr[3].split('"')

                obj_key = class_name + '.' + id_string
                if obj_key not in storage.all():
                    print("** no instance found **")
                else:
                    my_obj = storage.all()[obj_key]
                    my_obj.__dict__[attr_name] = str(attr_value[1])

                    my_obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
