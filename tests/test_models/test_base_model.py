#!/usr/bin/python3

"""The unittest for the BaseModel Class"""

import unittest
from models.base_model import BaseModel


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

    def test_str_method(self):
        """test str method"""
        self.assertEqual(str(self.bm),
                         f'[BaseModel] ({self.bm.id}) {self.bm.__dict__}')

    def test_save_method(self):
        """test self.update_at before and after the save method"""
        initial_updated_at = self.bm.updated_at
        self.bm.save()
        self.assertNotEqual(initial_updated_at, self.bm.updated_at)

    def test_to_dict_method_with_kwargs(self):
        """test to_dict method with kwargs"""
        bm_dict = self.bm.to_dict()
        self.assertEqual(bm_dict["__class__"], "BaseModel")
