import unittest
from decimal_to_roman import decimal_to_roman

class TestDecimalToRoman(unittest.TestCase):
    def test_positive_integer(self):
        self.assertEqual(decimal_to_roman(123), "CXXIII")

    def test_zero(self):
        self.assertEqual(decimal_to_roman(0), "Número fuera de rango")

    def test_negative_number(self):
        self.assertEqual(decimal_to_roman(-42), "Número fuera de rango")

    def test_max_value(self):
        self.assertEqual(decimal_to_roman(3999), "MMMCMXCIX")

    def test_decimal_number(self):
        self.assertEqual(decimal_to_roman(123.456), "Número fuera de rango")

if __name__ == "__main__":
    unittest.main()
