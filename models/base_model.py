#!/usr/bin/python3
""" Here goes everything, BaseModel, the start of AirBnb The console Project """
from uuid import uuid4
from datetime import datetime

class BaseModel():
    """ The Start  of the AirBnB project """

    def __init__(self):
        """ init """

        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        return (f'[{self.__class__.__name__}] ({self.id})  {self.__dict__}')

    def save(self):
        """ 
            updates the public instance attribute updated_at
            with the current datetime 
        """

        self.updated_at = datetime.now()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values
            of __dict__ of the instance
        """

        dict = obj_dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()

        return dict
