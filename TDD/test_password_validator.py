import unittest
from password_validator import is_password_secure

class TestPasswordValidator(unittest.TestCase):
    # At least 8 characters long
    def test_eight_characters(self):
        self.assertEqual(is_password_secure("EightCh1!"), True)  # Valid password
        self.assertEqual(is_password_secure("eight_ch"), False)  # Missing uppercase, digit, special char
        self.assertEqual(is_password_secure(""), False)          # Empty string

