#!/usr/bin/python3
"""unittest for the City Class"""
import unittest
from models.city import City
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage


class TestCity(unittest.TestCase):
    """The start of unittest for City Class"""

    def test_attributes(self):
        """test the initial values for every attribute in the class"""

        city = City()
        self.assertEqual(city.state_id, '')
        self.assertEqual(city.name, '')

    def test_to_dict_method(self):
        """test to_dict method that is from the BaseModel class"""

        city = City()
        city_dict = city.to_dict()
        self.assertTrue("__class__" in city_dict)
        self.assertTrue("created_at" in city_dict)
        self.assertTrue("updated_at" in city_dict)
        self.assertEqual(city_dict["__class__"], "City")
        self.assertEqual(city_dict["created_at"], city.created_at.isoformat())
        self.assertEqual(city_dict["updated_at"], city.updated_at.isoformat())

    def test_set_values(self):
        """assign values to the attributes of a City
            and check if they are set correctly
        """

        city = City()
        city.state_id = '123456'
        self.assertEqual(city.state_id, '123456')

        city.name = 'Cairo'
        self.assertEqual(city.name, 'Cairo')


class TestUserAndConsole(unittest.TestCase):
    """Test the City class with the console"""

    def setUp(self):
        """setting up the console to use it"""

        self.console = HBNBCommand()

    def test_update_city(self):
        """test city values before and after updating"""

        city = City()
        city.state_id = '123456'
        city.name = 'Cairo'

        # we will change the state_id from 123456 to 654321
        self.console.onecmd(f'update City {city.id} state_id "654321"')
        self.assertEqual(city.state_id, '654321')

        # name from Cairo to Alex
        self.console.onecmd(f'update City {city.id} name "Alex"')
        self.assertEqual(city.name, 'Alex')
