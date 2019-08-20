import unittest
from listutil import unique

class ListuTest(unittest.TestCase ):
    """Test the methods and constructor of the Fraction class. """

    def test_unique_empty_list(self) :
        self.assertEqual([],unique([]))
        

    def test_unique_one_item(self) :
        self.assertEqual(["a"],unique(["a"]))
        self.assertEqual(["car"],unique(["car"]))
        self.assertEqual(["anterio"],unique(["anterio"]))
        self.assertEqual([123],unique([123]))
        self.assertEqual([2456],unique([2456]))
        

    def test_unique_one_item_many_times(self) :
        self.assertEqual(["a"],unique(["a","a","a","a"]))
        self.assertEqual(["Miami"],unique(["Miami","Miami","Miami","Miami"]))
        self.assertEqual(["NewYork"],unique(["NewYork","NewYork","NewYork"]))
        
        
    def test_unique_two_item_many_times(self) :
        self.assertEqual(["a","b"],unique(["a","b","a","b","b","a","a","b"]))
        self.assertEqual(["Andy","Boba"],unique(["Andy","Boba","Boba","Andy","Andy","Boba"]))
        self.assertEqual(["NY","LA"],unique(["NY","NY","LA","LA","NY","LA","NY","LA"]))


    def test_unique_many_items_many_times(self):
        self.assertEqual(["a","b","c","d"],unique(["a","b","c","a","b","b","a","a","b","d"]))
        self.assertEqual(["Anne","Aura","Opal"],unique(["Anne","Aura","Opal","Aura","Opal","Anne"]))
        self.assertEqual(["Anne","Aura","Opal"],unique(["Anne","Aura","Opal","Aura","Opal","Anne"]))
        






    if __name__ == "__main__":
        unittest.main["listutil"]

    


