#!/usr/bin/python3
""" airbnb clone console program """
import cmd
import models
from models.user import User
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """ HBNB command class """
    prompt = '(hbnb) '
    class_dict = {"BaseModel": BaseModel, "User": User}

    def do_create(self, args):
        """ create instance """
        if not args:
            print("** class name messing **")
        else:
            if args in HBNBCommand.class_dict.keys():
                new_instance = HBNBCommand.class_dict[args]()
                models.storage.save()
                print(new_instance.id)
            else:
                print("** class doesn't exist **")

    def emptyline(self):
        """ handle empty line """
        pass

    def do_EOF(self, arg):
        """ handle EOF """
        return True

    def do_quit(self, arg):
        """ handle quit """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
