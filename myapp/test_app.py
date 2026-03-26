# test_app.py
import unittest
from app import add_numbers


class TestApp(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)  
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(1, 1), 2)

    def test_divide_numbers(self):
        from app import divide_numbers
        self.assertEqual(divide_numbers(6, 3), 2)
        self.assertEqual(divide_numbers(10, 2), 5)
        with self.assertRaises(ValueError):
            divide_numbers(5, 0)

if __name__ == "__main__":
    unittest.main()
