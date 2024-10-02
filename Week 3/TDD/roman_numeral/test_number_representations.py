import unittest
from number_representations import to_roman_numeral

class TestToRomanNumeral(unittest.TestCase):
    def test_zero(self):
        self.assertIsNone(to_roman_numeral(0)) 
