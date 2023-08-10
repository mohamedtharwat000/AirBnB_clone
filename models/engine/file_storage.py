#!/usr/bin/python3
""" FileStorage that serializes instances to a JSON file and deserializes JSON file to instances """
import json
from os.path import exists
from models.base_model import BaseModel
from datetime import datetime

class FileStorage():
    """ for serialization and deserialization """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id """

        FileStorage.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path) """

        # instances is a dict, and every key of it is an instance of BaseModel
        # and every value is the __dict__ of the instance
        obj = FileStorage.__objects
        instances = {key: obj.to_dict() for key, obj in obj.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(instances, f, indent=2)

    def reload(self):
        """ 
            Deserializes the JSON file to __objects
            only if the JSON file exists
            otherwise, do nothing.
        """

        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                instances = json.load(f)
                for key, objs in instances.items():
                    cls_name = objs['__class__']
                    cls_obj = globals()[cls_name]
                    for dt_attr in ['created_at', 'updated_at']:
                        dt_format = "%Y-%m-%dT%H:%M:%S.%f"
                        objs[dt_attr] = datetime.strptime(objs[dt_attr], dt_format)

                    instance = cls_obj(**objs)
                    FileStorage.__objects[key] = instance
        else:
            return
