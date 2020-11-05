#!/usr/bin/python3
"""Unittest module for the class city
"""
import unittest
import datetime
import models
from models.city import City
import os


class TestCity(unittest.TestCase):
    """methods of the test for class city
    """
    def test_documentation(self):
        """this checks all the documentation
        of all the methods of the class
        """
        self.assertIsNotNone(models.city.__doc__)
        self.assertIsNotNone(City.__doc__)

    def test_uniqueId(self):
        """this check if the instance
        that are created has a unique id
        """
        instance1 = City()
        instance2 = City()
        self.assertNotEqual(instance1, instance2)
        self.assertNotEqual(instance1.id, instance2.id)

    def test_exec_permissions(self):
        """Method that test for check the execution permissions
        """
        read = os.access('models/city.py', os.R_OK)
        self.assertTrue(read)
        write = os.access('models/city.py', os.W_OK)
        self.assertTrue(write)
        exect = os.access('models/city.py', os.X_OK)
        self.assertTrue(exect)

    def test_typeData(self):
        """this method check the type of
        the atributes when created a instance
        """
        instance1 = City()
        self.assertIsInstance(instance1.created_at, datetime.datetime)
        self.assertIsInstance(instance1.updated_at, datetime.datetime)
        self.assertIsInstance(instance1.id, str)
        self.assertIsInstance(instance1, City)

if __name__ == '__main__':
    unittest.main()
