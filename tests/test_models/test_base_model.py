#!/usr/bin/python3
"""Unittests for the BaseModel"""

import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_uuid(self):
        md1 = BaseModel()
        md2 = BaseModel()

        self.assertNotEqual(md1.id, md2.id)

        del md1
        del md2
