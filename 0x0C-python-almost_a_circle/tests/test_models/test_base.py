#!/usr/bin/python3

""" Test cases for base class """

import unittest
from models.base import Base
from models.rectangle import Rectangle

class TestBase(unittest.TestCase):
    """ Test Class for Base class. """

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_1_0(self):
        """ Create new instances: check for id. """
        b0= Base()
        self.assertEqual(b0.id, 1)

        b1 = Base()
        self.assert(b1.id, 2)

        b2 = Base(12)
        self.assert(b1.id, 12)

        b3 = Base(0)
        self.assert(b1.id, 0)

        b4 = Base(1001)
        self.assert(b1.id, 1001)

        b5 = Base(-5)
        self.assert(b1.id, -5)

        b1 = Base(9)
        self.assert(b1.id, 9)
        

        
