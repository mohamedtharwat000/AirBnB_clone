#!/usr/bin/python3

"""Unit tests for the FileStorage Class"""

from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import unittest
import json
from os.path import exists


class TestFileStorage(unittest.TestCase):
    """Unit tests for the FileStorage Class"""

    @classmethod
    def setUpClass(cls):
        """Set up test environment"""
        cls.fs = FileStorage()

    def test_new_instance(self):
        """Test creating a new instance of FileStorage"""
        self.assertIsInstance(self.fs, FileStorage)
        self.assertTrue(self.fs.all(), {})

    def test_all(self):
        """Test all method"""
        self.assertIsInstance(self.fs.all(), dict)

    def test_new(self):
        """Test the 'all' method and creating new objects"""
        self.bm = BaseModel()
        self.fs.new(self.bm)
        self.assertEqual(self.fs.all()[f"BaseModel.{self.bm.id}"], self.bm)

    def test_save(self):
        """Test the 'save' method and JSON file creation"""
        self.bm = BaseModel()
        self.fs.new(self.bm)
        self.fs.save()
        self.assertTrue(exists("./file.json"))
        with open("./file.json", "r") as file:
            self.assertEqual(json.load(file)[f"BaseModel.{self.bm.id}"],
                                                            self.bm.to_dict())

    def test_reload(self):
        """Test the 'reload' method"""
        self.bm = BaseModel()
        self.fs.new(self.bm)
        self.fs.save()
        self.fs.reload()
        self.assertEqual(self.fs.all()[f"BaseModel.{self.bm.id}"].id,
                                                            self.bm.id)
