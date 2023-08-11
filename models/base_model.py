#!/usr/bin/python3

"""
    Here goes everything, BaseModel, the start of AirBnb The console Project
"""

import models
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
        This is the base model of the AirBnB project
    """

    def __init__(self, *args, **kwargs):
        """
            __init__ - class constructor
            Args:
                args: list of arguments
                kwargs: dictionary of arguments
        """
        if kwargs:
            for key, val in kwargs.items():
                if key == '__class__':
                    continue
                elif (key == 'created_at' or key == 'updated_at') \
                        and type(val) is str:
                    dt_format = "%Y-%m-%dT%H:%M:%S.%f"
                    setattr(self, key, datetime.strptime(val, dt_format))
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """
            returns a string representation of the class instance
        """
        return (f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}')

    def save(self):
        """
            updates the public instance attribute updated_at
            with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values
            of __dict__ of the instance
        """
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
