import math

class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """
    
    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """

        if denominator == 0 :
            if numerator == 0 :
                raise ValueError
            elif numerator > 0 :
                numerator = 1
                denominator = 0
            elif numerator < 0 :
                numerator = -1 
                denominator = 0
        elif numerator < 0 and denominator < 0 :
            numerator = abs(numerator)
            denominator = abs(denominator)
        elif numerator > 0 and denominator < 0 :
            numerator = -numerator
            denominator = abs(denominator)
        
        self.numerator = numerator//math.gcd(numerator,denominator)
        self.denominator = denominator//math.gcd(numerator,denominator)


    def __str__(self):
        """returns the string representation of the object.
        """
        if self.numerator % self.denominator == 0:
            return f"{int(self.numerator / self.denominator)}"
        return f"{int(self.numerator)}/{int(self.denominator)}"

        # if self.numerator % self.denominator == 0 :
        #     return str(int(self.numerator/self.denominator))
        # else :
        #     return f"{self.numerator}/{self.denominator}"


    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        numerator = ((self.numerator * frac.denominator)+(self.denominator * frac.numerator))
        denominator = (self.denominator * frac.denominator)
    
        return Fraction(numerator,denominator)


    def __sub__(self, frac):
        """Return the substraction of two fractions as a new fraction.
        Use the standard formula  a/b - c/d = (ad-bc)/(b*d)
        """
        numerator = ((self.numerator * frac.denominator)-(self.denominator * frac.numerator))
        denominator = (self.denominator * frac.denominator)
    
        return Fraction(numerator,denominator)


    def __mul__(self,frac) :
        """Return the multiple of two fractions as a new fraction.
        """
        numerator = self.numerator * frac.numerator
        denominator = self.denominator * frac.denominator

        return Fraction(numerator,denominator)


    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator


    def __gt__(self,frac) :
         
        first = self.numerator * frac.denominator
        second = self.denominator * frac.numerator

        return first > second

        
    def __neg__(self) :
         
        return Fraction(-self.numerator,self.denominator)

   
    
