#!/usr/bin/python3

"""
    file_storage module that
    1- stores instances to a JSON file
    2- loads instances from a JSON file
"""
import json
from os.path import exists
from datetime import datetime
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage():
    """
        FileStorage class for serialization and deserialization
    """
    __file_path = "./file.json"
    __objects = {}

    def all(self):
        """
            all - return the dictionary __objects
        """
        return self.__class__.__objects

    def new(self, obj):
        """
            new - add obj to __objects
        """
        self.__class__.__objects[f'{obj.__class__.__name__}.{obj.id}'] = obj

    def save(self):
        """
            serializes __objects to the JSON file (path: __file_path)
        """
        objects = self.__class__.__objects
        instances = {key: obj.to_dict() for key, obj in objects.items()}
        with open(self.__class__.__file_path, "w") as file:
            json.dump(instances, file)

    def reload(self):
        """
            Deserializes the JSON file to __objects
            only if the JSON file exists
            otherwise, do nothing.
        """
        if exists(self.__class__.__file_path):
            with open(self.__class__.__file_path, "r") as file:
                instances = json.load(file)
                new_objects = {}
                for key, objs in instances.items():
                    for dt in ['created_at', 'updated_at']:
                        dt_format = "%Y-%m-%dT%H:%M:%S.%f"
                        objs[dt] = datetime.strptime(objs[dt], dt_format)
                    new_objects[key] = BaseModel(**objs)
                self.__class__.__objects = new_objects
