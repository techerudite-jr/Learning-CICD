# test_app.py
import unittest
from app import add_numbers

class TestApp(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 7)  # Simulated conflicting change in main
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_subtract_numbers(self):
        from app import subtract_numbers
        self.assertEqual(subtract_numbers(5, 3), 2)
        self.assertEqual(subtract_numbers(0, 1), -1)
        self.assertEqual(subtract_numbers(10, 5), 5)

if __name__ == "__main__":
    unittest.main()
