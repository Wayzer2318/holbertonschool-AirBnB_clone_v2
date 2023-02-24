#!/usr/bin/python3
""" airbnb clone console program """
import cmd


class HBNBCommand(cmd.Cmd):
    """ HBNB command class """
    prompt = '(hbnb) '

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
