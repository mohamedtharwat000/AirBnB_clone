#!/usr/bin/python3

"""Unit tests for the FileStorage Class."""

import unittest
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from os import remove
from os.path import exists


class TestFileStorage(unittest.TestCase):
    """Unit tests for the FileStorage Class."""

    @classmethod
    def setUpClass(cls):
        """Set up test environment."""
        cls.fs = FileStorage()

    @classmethod
    def tearDownClass(cls):
        """Tear down test environment."""
        del cls.fs
        if exists("./file.json"):
            remove("./file.json")

    def tearDown(self):
        """Tear down test environment."""
        self.__class__.fs._FileStorage__objects = {}
        try:
            del self.bm
        except AttributeError:
            pass

    def test_attributes(self):
        """Test the existence of FileStorage Class Attirbutes."""
        self.assertTrue(hasattr(self.__class__.fs, "_FileStorage__file_path"))
        self.assertTrue(hasattr(self.__class__.fs, "_FileStorage__objects"))

    def test_all(self):
        """Test all method."""
        self.assertIsInstance(self.__class__.fs, FileStorage)
        self.assertIsInstance(self.__class__.fs.all(), dict)
        self.assertIs(self.__class__.fs.all(),
                      self.__class__.fs._FileStorage__objects)

    def test_new(self):
        """Test the 'all' method and creating new objects."""
        self.bm = BaseModel()
        self.__class__.fs.new(self.bm)
        cls_name = self.bm.__class__.__name__
        self.assertEqual(self.__class__.fs.all()[f"{cls_name}.{self.bm.id}"],
                         self.bm)

    def test_save(self):
        """Test the 'save' method and JSON file creation."""
        self.bm = BaseModel()
        self.__class__.fs.new(self.bm)
        self.__class__.fs.save()
        self.assertTrue(exists("./file.json"))
        with open("./file.json", "r") as file:
            cls_name = self.bm.__class__.__name__
            self.assertEqual(json.load(file)[f"{cls_name}.{self.bm.id}"],
                             self.bm.to_dict())

    def test_reload(self):
        """Test the 'reload' method."""
        self.bm = BaseModel()
        self.__class__.fs.new(self.bm)
        self.__class__.fs.save()
        self.__class__.fs.reload()
        cls_name = self.bm.__class__.__name__
        self.assertEqual(
            self.__class__.fs.all()[f"{cls_name}.{self.bm.id}"].id, self.bm.id)

    def test_reload_v2(self):
        """Tests method: reload (reloads objects from string file)."""
        try:
            remove("file.json")
        except Exception:
            pass
        with open("file.json", "w") as file:
            file.write("{}")
        with open("file.json", "r") as file:
            self.assertEqual(json.load(file), {})
            self.__class__.fs.reload()
            self.assertEqual(self.__class__.fs.all(), {})

    def test_new_duplicate(self):
        """Test new method with duplicate objects."""
        self.bm = BaseModel()
        self.bm2 = BaseModel()
        self.__class__.fs.new(self.bm)
        ln = len(self.__class__.fs._FileStorage__objects)
        self.__class__.fs.new(self.bm2)
        self.assertEqual(len(self.__class__.fs._FileStorage__objects), ln)

    def test_new_invalid_input(self):
        """Test the new method with an invalid input."""
        with self.assertRaises(AttributeError):
            self.__class__.fs.new("input_should_be_an_obk")

    def test_save_invalid_input(self):
        """Test save method, passing an invalid input."""
        with self.assertRaises(TypeError):
            self.__class__.fs.save("invalid_input")
