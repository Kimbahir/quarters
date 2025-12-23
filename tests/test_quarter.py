import unittest
from datetime import date
from quarters import Quarter

class TestQuarter(unittest.TestCase):
    def test_from_date(self):
        self.assertEqual(Quarter.from_date(date(2023, 2, 15)), Quarter(2023, 1))
        self.assertEqual(Quarter.from_date(date(2023, 5, 1)), Quarter(2023, 2))

    def test_to_date(self):
        self.assertEqual(Quarter(2023, 1).to_date(), date(2023, 1, 1))
        self.assertEqual(Quarter(2023, 4).to_date(), date(2023, 10, 1))

    def test_str(self):
        self.assertEqual(str(Quarter(2023, 3)), "Q3 2023")

    def test_add_quarters(self):
        self.assertEqual(Quarter(2023, 4).add_quarters(1), Quarter(2024, 1))
        self.assertEqual(Quarter(2023, 1).add_quarters(-1), Quarter(2022, 4))

    def test_invalid_quarter(self):
        with self.assertRaises(ValueError):
            Quarter(2023, 0)
        with self.assertRaises(ValueError):
            Quarter(2023, 5)

if __name__ == "__main__":
    unittest.main()
