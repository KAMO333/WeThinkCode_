import unittest
from password_validator import is_password_secure

class TestPasswordValidator(unittest.TestCase):
    # At least 8 characters long
    def test_eight_characters(self):
        self.assertEqual(is_password_secure("EightCh1!"), True)  # Valid password
        self.assertEqual(is_password_secure("eight_ch"), False)  # Missing uppercase, digit, special char
        self.assertEqual(is_password_secure(""), False)          # Empty string


    
    # Contains both uppercase and lowercase letters
    def test_upper_char(self):
        self.assertTrue(is_password_secure("EightChar1!"), "Expecting True")  # Valid password
        self.assertFalse(is_password_secure("eight_char1!"), "Expecting False")  # No uppercase
        self.assertFalse(is_password_secure("EIGHT_CHAR1!"), "Expecting False")  # No lowercase

    # Has at least one digit
    def test_one_digit(self):
        self.assertTrue(is_password_secure("EightChar1!"), "Expecting True")  # Valid password
        self.assertFalse(is_password_secure("EightChar!"), "Expecting False")  # No digit

    # Has at least one special character
    def test_special_char(self):
        self.assertTrue(is_password_secure("EightChar1!"), "Was expecting True")  # Valid password
        self.assertFalse(is_password_secure("EightChar1"), "Was expecting False")  # No special char

if __name__ == '__main__':
    unittest.main()



