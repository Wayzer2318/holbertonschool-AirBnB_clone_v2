#!/usr/bin/python3

import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ test for file storage """

    def setUp(self):
        """ set up """
        self.my_model = BaseModel()
        self.my_storage = FileStorage()

    def test_new(self):
        """ test new """
        self.my_storage.new(self.my_model)
        new_dict = self.my_storage.all()
        key = self.my_model.__class__.__name__ + "." + self.my_model.id
        self.assertIsInstance(new_dict[key], BaseModel)

    def test_all(self):
        """ test all """
        self.assertIsInstance(self.my_storage.all(), dict)

    def test_save(self):
        """ test save """
        self.my_storage.save()
        self.assertTrue(os.path.exists("file.json"))


