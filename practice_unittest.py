import math
import time
import unittest
from fraction import Fraction

class FractionTest(unittest.TestCase) :
    """Test the methods and constructor of the Fraction class. """
    def test_str(self) :
        f = Fraction(3,10)
        self.assertEqual("3/10",f.__str__())
        f = Fraction(-3,1)
        self.assertEqual("-3",f.__str__())

    def test_add(self) :
        self.assertEqual(Fraction(1,2), Fraction(1,4)+Fraction(1,4))
        self.assertEqual(Fraction(25,28), Fraction(3,4)+Fraction(1,7))
        self.assertEqual(Fraction(38,45), Fraction(4,9)+Fraction(2,5))
        self.assertEqual(Fraction(1,1), Fraction(1,5)+Fraction(4,5))


    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001)
        self.assertTrue(f==g)
        self.assertTrue(f.__eq__(g))
        