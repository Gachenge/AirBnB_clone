#!/usr/bin/python3
import cmd
import sys
"""class cmd is here to help us run the project from the console"""


class HBNBCommand(cmd.Cmd):
    """here we will add methods in order to run all the basic
    commands on the project
    We shall use our own personal prompt
    """
    def __init__(self):
        """initialise the classs and introduce a custom prompt"""
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def do_EOF(self, line):
        """to catch the end of file and control+ D"""
        return True

    def do_quit(self, line):
        """the quit command should exit the programe"""
        sys.exit(1)

    def emptyline(self):
        """an empty line + enter shouldn't execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
