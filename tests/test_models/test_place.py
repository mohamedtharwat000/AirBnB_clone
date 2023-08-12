#!/use/bin/python3
"""unittest for the Place Class"""
import unittest
from models.place import Place
from datetime import datetime
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage


class TestPlace(unittest.TestCase):
    """The start of unittest for Place Class"""

    def test_attributes(self):
        """test the initial values for every attribute in the class"""

        place = Place()
        self.assertEqual(place.city_id, '')
        self.assertEqual(place.user_id, '')
        self.assertEqual(place.name, '')
        self.assertEqual(place.description, '')
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_to_dict_method(self):
        """test to_dict method that is from the BaseModel class"""

        place = Place()
        place_dict = place.to_dict()
        self.assertTrue("__class__" in place_dict)
        self.assertTrue("created_at" in place_dict)
        self.assertTrue("updated_at" in place_dict)
        self.assertEqual(place_dict["__class__"], "Place")
        tmp_1 = place.created_at.isoformat()
        tmp_2 = place.updated_at.isoformat()
        self.assertEqual(place_dict["created_at"], tmp_1)
        self.assertEqual(place_dict["updated_at"], tmp_2)

    def test_set_values(self):
        """assign values to the attributes of a Place
            and check if they are set correctly
        """

        place = Place()
        place.city_id = 'ABC-123'
        place.user_id = 'ABC-123'
        place.name = 'Duqqi'
        place.description = 'Good place to visit'
        place.number_rooms = 10
        place.number_bathrooms = 2
        place.max_guest = 25
        place.price_by_night = 125
        place.latitude = 5.6
        place.longitude = 10.4
        place.amenity_ids = ['123', '456', '789']

        self.assertEqual(place.city_id, 'ABC-123')
        self.assertEqual(place.user_id, 'ABC-123')
        self.assertEqual(place.name, 'Duqqi')
        self.assertEqual(place.description, 'Good place to visit')
        self.assertEqual(place.number_rooms, 10)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 25)
        self.assertEqual(place.price_by_night, 125)
        self.assertEqual(place.latitude, 5.6)
        self.assertEqual(place.longitude, 10.4)
        self.assertEqual(place.amenity_ids, ['123', '456', '789'])
