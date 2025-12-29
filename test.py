import unittest
from app import calculate_sum  # <-- Важливо: має бути саме ця назва

class TestProgression(unittest.TestCase):
    
    def test_positive(self):
        self.assertEqual(calculate_sum(3), 12)

    def test_zero(self):
        self.assertEqual(calculate_sum(0), 0)

    def test_negative(self):
        with self.assertRaises(ValueError):
            calculate_sum(-1)

if __name__ == '__main__':
    unittest.main()