import unittest
from cash_register import change

class TestChange(unittest.TestCase):
    def test_small_change(self):
        self.assertEqual(change(250, 1000), {'R5': 1, 'R2': 1, '50c': 1})
        self.assertEqual(change(300, 500), {'R2': 1})
        self.assertEqual(change(50, 100), {'50c': 1})
        self.assertEqual(change(25, 100), {'50c': 1, '20c': 1, '5c': 1})
        self.assertEqual(change(200, 500), {'R2': 1, 'R1': 1})
    
    def test_medium_change(self):
        self.assertEqual(change(2300, 5000), {'R20': 1, 'R5': 1, 'R2': 1})
        self.assertEqual(change(1000, 2500), {'R10': 1, 'R5': 1})
        self.assertEqual(change(2550, 6000), {'R20': 1, 'R10': 1, 'R2': 2, '50c': 1})
        self.assertEqual(change(600, 1200), {'R5':1, 'R1': 1})

