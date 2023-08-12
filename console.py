#!/usr/bin/python3

"""entry point of the command interpreter."""

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Entry to command interpreter."""

    prompt = "(hbnb) "
    classes = [BaseModel, User, State, City, Amenity, Place, Review]

    def do_EOF(self, line):
        """Exit on Ctrl-D (EOF)."""
        print()
        return True

    def do_quit(self, line):
        """Exit on quit."""
        return True

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_create(self, line):
        """Create instance specified by user.

        Args:
            line: class name
        """
        if not line:
            print("** class name missing **")
        elif line not in [cls.__name__ for cls in HBNBCommand.classes]:
            print("** class doesn't exist **")
        else:
            instance = None
            for cls in HBNBCommand.classes:
                if line == cls.__name__:
                    instance = cls()
                    instance.save()
                    print(instance.id)

    def do_show(self, line):
        """Print string representation: name and id.

        Args:
            line: class name and id
        """
        if not line:
            print("** class name missing **")
            return
        args = parse_line(line)
        if args[0] not in [cls.__name__ for cls in HBNBCommand.classes]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        name = f"{args[0]}.{args[1]}"
        if name not in models.storage.all().keys():
            print("** no instance found **")
            return
        print(models.storage.all()[name])

    def do_destroy(self, line):
        """Destroy instance and Save changes to JSON file.

        Args:
            line: class name
        """
        if not line:
            print("** class name missing **")
            return
        args = parse_line(line)
        if args[0] not in [cls.__name__ for cls in HBNBCommand.classes]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        name = f"{args[0]}.{args[1]}"
        if name not in models.storage.all().keys():
            print("** no instance found **")
            return
        models.storage.all().pop(name)
        models.storage.save()

    def do_all(self, line):
        """Print all objects or all objects of specified class.

        Args:
            line: class name
        """
        obj_list = []
        if not line:
            for objs in models.storage.all().values():
                obj_list.append(str(objs))
            print(obj_list)
            return
        args = parse_line(line)
        if args[0] not in [cls.__name__ for cls in HBNBCommand.classes]:
            print("** class doesn't exist **")
            return
        for key, objs in models.storage.all().items():
            if key.startswith(args[0]):
                obj_list.append(str(objs))
        print(obj_list)

    def do_update(self, line):
        """Update if given exact object, exact attribute.

        Args:
            line: class name, id, attribute, value
        """
        if not line:
            print("** class name missing **")
            return
        args = parse_line(line)
        if args[0] not in [cls.__name__ for cls in HBNBCommand.classes]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        name = f"{args[0]}.{args[1]}"
        if name not in models.storage.all().keys():
            print("** no instance found **")
            return
        attr_val = args[3]
        type_val = type(eval(attr_val))
        attr_val = attr_val.strip('"')
        setattr(models.storage.all()[name], args[2], type_val(attr_val))
        models.storage.save()


def parse_line(line):
    """Split user typed input."""
    return line.split()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
