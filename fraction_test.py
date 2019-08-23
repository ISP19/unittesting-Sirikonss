import math
import time
import unittest
from fraction import Fraction


class FractionTest(unittest.TestCase):
    """Test the methods and constructor of the Fraction class. """

    def test_str(self):
        f = Fraction(3, -1)
        self.assertEqual("-3", f.__str__())
        f = Fraction(0, 5)
        self.assertEqual("0", f.__str__())
        f = Fraction(60, 90)
        self.assertEqual("2/3", f.__str__())
        f = Fraction(1500, 60)
        self.assertEqual("25", f.__str__())
        f = Fraction(1500, 90)
        self.assertEqual("50/3", f.__str__())
        f = Fraction(-80, 20)
        self.assertEqual("-4", f.__str__())
        f = Fraction(36, -60)
        self.assertEqual("-3/5", f.__str__())

        # Constructor should provide default denominator = 1
        f = Fraction(99)
        self.assertEqual("99", f.__str__())
        f = Fraction(-32)
        self.assertEqual("-32", f.__str__())
        f = Fraction(0)
        self.assertEqual("0", f.__str__())


    def test_add(self):
        # 3/4 = 2/3 + 1/12
        self.assertEqual(Fraction(0,0), Fraction(0,0)+Fraction(1,3))
        self.assertEqual(Fraction(3,4), Fraction(1,12)+Fraction(2,3))
        self.assertEqual(Fraction(1,15), Fraction(1,15)+Fraction(0))
        self.assertEqual(Fraction(-7,30), Fraction(-2,5)+Fraction(1,6))
        self.assertEqual(Fraction(-5,12), Fraction(1,4)+Fraction(2,-3))
        self.assertEqual(Fraction(-31,18), Fraction(-5,6)+Fraction(-8,9))


    def test_sub(self):
        # -7/12 = 1/12 - 2/3
        self.assertEqual(Fraction(0,0), Fraction(0,0)-Fraction(1,3))
        self.assertEqual(Fraction(-7,12), Fraction(1,12)-Fraction(2,3))
        self.assertEqual(Fraction(7,20), Fraction(3,4)-Fraction(2,5))
        self.assertEqual(Fraction(-3,13), Fraction(-10,13)-Fraction(14,-26))
        self.assertEqual(Fraction(37,40), Fraction(4,5)-Fraction(-1,8))
        self.assertEqual(Fraction(22,-63), Fraction(2,9)-Fraction(4,7))


    def test_mul(self):
        # 1/18 = 1/12 * 2/3
        self.assertEqual(Fraction(0,0), Fraction(0,0)*Fraction(1,3))
        self.assertEqual(Fraction(1,18), Fraction(1,12)*Fraction(2,3))
        self.assertEqual(Fraction(-1,15), Fraction(-2,5)*Fraction(1,6))
        self.assertEqual(Fraction(1,-6), Fraction(1,4)*Fraction(2,-3))
        self.assertEqual(Fraction(1,-10), Fraction(4,5)*Fraction(-1,8))
        self.assertEqual(Fraction(12,35), Fraction(4,7)*Fraction(3,5))
        
    
    def test_eq(self):
        f = Fraction(1,2)
        g = Fraction(-40,-80)
        h = Fraction(10000,20001) # not quite 1/2
        self.assertTrue(f == g)
        self.assertTrue(f.__eq__(g))  # same thing
        self.assertFalse(f == h)
        self.assertFalse(f.__eq__(h))
        f = Fraction(-13,29)
        g = Fraction(-16,36)
        h = Fraction(26,-58) 
        self.assertTrue(f == h)
        self.assertTrue(f.__eq__(h))  # same thing
        self.assertFalse(f == g)
        self.assertFalse(f.__eq__(g)) 
        f = Fraction(-1,0)
        g = Fraction(2,0)
        h = Fraction(0,1) 
        self.assertFalse(g == h)
        self.assertFalse(g.__eq__(h))  # same thing
        self.assertFalse(f == g)
        self.assertFalse(f.__eq__(g)) 


    def test_gt(self):
        
        f = Fraction(4,5)
        g = Fraction(7,8)
        self.assertFalse(f.__gt__(g))
        self.assertTrue(g.__gt__(f))
        f = Fraction(2,7)
        g = Fraction(3,5)
        self.assertFalse(f.__gt__(g))
        self.assertTrue(g.__gt__(f))
        f = Fraction(8,9)
        g = Fraction(-1,2)
        self.assertTrue(f.__gt__(g))
        self.assertFalse(g.__gt__(f))
        f = Fraction(-11,17)
        g = Fraction(22,-39)
        self.assertFalse(f.__gt__(g))
        self.assertTrue(g.__gt__(f))
        f = Fraction(-18,29)
        g = Fraction(-15,21)
        self.assertTrue(f.__gt__(g))
        self.assertFalse(g.__gt__(f))

    def test_neg(self) :
        self.assertEqual(Fraction(-7,12), -Fraction(7,12))
        self.assertEqual(Fraction(3,5), -Fraction(-6,10))
        self.assertEqual(Fraction(-8), -Fraction(24,3))
        self.assertEqual(Fraction(-1,3), -Fraction(-3,-9))
        self.assertEqual(Fraction(-1,0), -Fraction(1,0))



        
    
        
