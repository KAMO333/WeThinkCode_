import unittest
from number_representations import to_roman_numeral

class TestToRomanNumeral(unittest.TestCase):
    def test_zero(self):
        self.assertIsNone(to_roman_numeral(0)) 

    def test_single_digit(self):
        self.assertEqual(to_roman_numeral(1), "I")
        self.assertEqual(to_roman_numeral(3), "III")
        self.assertEqual(to_roman_numeral(4), "IV")
        self.assertEqual(to_roman_numeral(9), "IX") 

