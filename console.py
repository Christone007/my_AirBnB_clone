#!/usr/bin/python3
"""This module defines a Command Line Interpreter for the program"""

import cmd


class MyInterpreter(cmd.Cmd):
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

    def do_foo(self, line):
        """Test function which just prints to stdout"""
        print("The foo method has been called")


if __name__ == "__main__":
    MyInterpreter().cmdloop()
