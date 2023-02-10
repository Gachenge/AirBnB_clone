#!/usr/bin/python3
import cmd, sys, re
from shlex import split
from models.base_model import BaseModel
from models import storage
from models.user import User

"""class cmd is here to help us run the project from the console"""

def parse(arg):
    """splits the arguments"""
    brace = re.search(r"\{(.*?)\}", arg)
    brack = re.search(r"\[(.*?)\]", arg)
    if brace is None:
        if brack is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lex = split(arg[:brack.span()[0]])
            ret = [i.strip(",") for i in lex]
            ret.append(brack.group())
            return ret
    else:
        lex = split(arg[:brace.span()[0]])
        ret = [i.strip(",") for i in lex]
        ret.append(brace.group())
        return ret


class HBNBCommand(cmd.Cmd):
    """here we will add methods in order to run all the basic
    commands on the project
    We shall use our own personal prompt
    """
    prompt = '(hbnb) '
    __classes = {
        "BaseModel",
        "User"
    }
    
    def do_EOF(self, line):
        """to catch the end of file and control+ D"""
        return True

    def do_quit(self, line):
        """the quit command should exit the programe"""
        sys.exit(1)

    def emptyline(self):
        """overide new line to no execute anything"""
        pass        

    def do_create(self, args):
        """creates a new instance of BaseModel"""
        arg1 = parse(args)
        if len(arg1) == 0:
            print("** class name missing **")
        elif arg1[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            storage.save()
            print(eval(arg1[0])().id)

    def do_show(self, args):
        """Prints the string representation of an instance based on the class name and id"""
        arg1 = parse(args)
        obj = storage.all()
        if len(arg1) == 0:
            print("** class name missing")
        elif arg1[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg1[0], arg1[1]) not in obj:
            print("** no instance found **")
        else:
            print(obj["{}.{}".format(arg1[0], arg1[1])])

    def do_destroy(self, args):
        """destroy or delete an instance of a class"""
        arg = parse(args)
        obj = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj.keys():
            print("** no instance found **")
        else:
            del(obj["{}.{}".format(arg[0], arg[1])])
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()