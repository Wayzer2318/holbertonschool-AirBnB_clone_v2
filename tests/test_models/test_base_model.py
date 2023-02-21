#!/usr/bin/python3

import unittest

from models.base_model import BaseModel


class Test_Base(unittest.TestCase):
    def test_id_is_str(self):
        model = BaseModel()
        self.assertEqual(str(type(model.id)), "<class 'str'>")

    def test_created_is_dtobj(self):
        model = BaseModel()
        self.assertEqual(str(type(model.created_at)), "<class 'datetime.datetime'>")

    def test_updated_is_dtobj(self):
        model = BaseModel()
        self.assertEqual(str(type(model.updated_at)), "<class 'datetime.datetime'>")
