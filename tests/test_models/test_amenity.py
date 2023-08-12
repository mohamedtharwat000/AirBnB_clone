#!/use/bin/python3
"""unittest for the Amenity Class"""
import unittest
from models.amenity import Amenity
from datetime import datetime
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage


class TestAmenity(unittest.TestCase):
    """The start of unittest for Amenity Class"""

    def test_attributes(self):
        """test the initial values for every attribute in the class"""

        amenity = Amenity()
        self.assertEqual(amenity.name, '')

    def test_to_dict_method(self):
        """test to_dict method that is from the BaseModel class"""

        amenity = Amenity()
        amenity_dict = amenity.to_dict()
        self.assertTrue("__class__" in amenity_dict)
        self.assertTrue("created_at" in amenity_dict)
        self.assertTrue("updated_at" in amenity_dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        tmp_1 = amenity.created_at.isoformat()
        tmp_2 = amenity.updated_at.isoformat()
        self.assertEqual(amenity_dict["created_at"], tmp_1)
        self.assertEqual(amenity_dict["updated_at"], tmp_2)

    def test_set_values(self):
        """assign values to the attributes of a Amenity
            and check if they are set correctly
        """

        amenity = Amenity()
        amenity.name = 'Good'
        self.assertEqual(amenity.name, 'Good')


class TestUserAndConsole(unittest.TestCase):
    """Test the Amenity class with the console"""

    def setUp(self):
        """setting up the console to use it"""

        self.console = HBNBCommand()

    def test_update_amenity(self):
        """test amenity values before and after updating"""

        amenity = Amenity()
        amenity.name = 'Bad'

        # we will change the amenity from Bad to Perfect
        self.console.onecmd(f'update Amenity {amenity.id} name "Perfect"')
        self.assertEqual(amenity.name, 'Perfect')
