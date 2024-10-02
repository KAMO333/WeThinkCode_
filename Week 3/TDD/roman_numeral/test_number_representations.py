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

    def test_double_digits(self):
        self.assertEqual(to_roman_numeral(12), "XII")
        self.assertEqual(to_roman_numeral(27), "XXVII")
        self.assertEqual(to_roman_numeral(40), "XL")

    def test_triple_digits(self):
        self.assertEqual(to_roman_numeral(90), "XC")
        self.assertEqual(to_roman_numeral(148), "CXLVIII")
        self.assertEqual(to_roman_numeral(400), "CD")
        self.assertEqual(to_roman_numeral(900), "CM")

    def test_quadruple(self):
        self.assertEqual(to_roman_numeral(1994), "MCMXCIV")
        self.assertEqual(to_roman_numeral(3999), "MMMCMXCIX")

    # Tests for invalid types like string and float
    def test_invalid_string(self):
        # Strings should raise an error
        with self.assertRaises(TypeError):
            to_roman_numeral("ten") 




