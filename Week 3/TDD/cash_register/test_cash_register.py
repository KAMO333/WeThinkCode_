import unittest
from cash_register import change

class TestChange(unittest.TestCase):
    def test_small_change(self):
        self.assertEqual(change(250, 1000), {'R5': 1, 'R2': 1, '50c': 1})
        self.assertEqual(change(300, 500), {'R2': 1})
        self.assertEqual(change(50, 100), {'50c': 1})
        self.assertEqual(change(25, 100), {'50c': 1, '20c': 1, '5c': 1})
        self.assertEqual(change(200, 500), {'R2': 1, 'R1': 1})

