#!/usr/bin/python3
"""The unittest for the BaseModel Class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from models import storage


class TestBaseModel(unittest.TestCase):
    """The start of unittest for BaseModel Class"""

    def setUp(self):
        """setint up an instance of BaseModel"""
        self.bm = BaseModel()

    def test_new_instance(self):
        """tests the values of an intanct of BaseModel"""

        self.assertIsInstance(self.bm, BaseModel)
        self.assertIsNotNone(self.bm.id)
        self.assertIsNotNone(self.bm.created_at)
        self.assertIsNotNone(self.bm.updated_at)

    def test_to_dict_method(self):
        """test to_dict method"""

        bm_dict = self.bm.to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")
        self.assertTrue("__class__" in bm_dict)
        self.assertTrue("created_at" in bm_dict)
        self.assertTrue("updated_at" in bm_dict)
        self.assertTrue("id" in bm_dict)

    def test_save_method(self):
        """test self.update_at before and after the save method"""

        initial_updated_at = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(initial_updated_at, self.bm.updated_at)

    def test_reload_method(self):
        """test reload method which is from FileStorage Class"""

        self.bm.name = 'Mohammed'
        self.bm.save()
        storage.reload()

        reloaded_bm = storage.all()[f'{self.bm.__class__.__name__}'
                                    f'.{self.bm.id}']

        self.assertEqual(reloaded_bm.name, 'Mohammed')
