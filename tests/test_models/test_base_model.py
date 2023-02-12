#!/usr/bin/python3

import unittest
import models
from models.base_model import BaseModel

"""Tests for the BaseModel"""


class TestBase(unittest.TestCase):
    """test all the functions of the basemodel class"""
    def test_noarg(self):
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_not(self):
        self.assertIsNotNone(type(BaseModel().id))
        
    def test_uniqid(self):
        self.assertNotEqual(BaseModel().id, BaseModel().id)
    
    def test_stor(self):
        self.assertIn(BaseModel(), models.storage.all().values())
    
    def test_isidstr(self):
        self.assertEqual(type(BaseModel().id), str)

    def test_difcreated(self):
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(b.created_at, a.created_at)

    def test_difupdate(self):
        a = BaseModel()
        b = BaseModel()
        self.assertNotEqual(a.updated_at, b.updated_at)

    def test_saveUpdate(self):
        a = BaseModel()
        b = a.updated_at
        a.save()
        self.assertLess(b, a.updated_at)

    def test_savetwo(self):
        a = BaseModel()
        b = BaseModel()
        a.save()
        b.save()
        with open('file.json') as f:
            self.assertIn(a.id, f.read())
        with open('file.json') as f:
            self.assertIn(b.id, f.read())

    def test_strfun(self):
        a = BaseModel()
        self.assertEqual(a.__str__(), "[BaseModel] ({}) {}".format(a.id, a.__dict__.copy()))

    def test_dict(self):
        a = BaseModel()
        b = a.to_dict()
        self.assertEqual(b["created_at"], b["updated_at"])

if __name__ == "__main__":
    unittest.main()