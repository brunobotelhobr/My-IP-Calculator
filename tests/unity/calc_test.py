"""Test the calc module."""
import unittest

from app.calc import Calculator

calc = Calculator()


class TestCalc(unittest.TestCase):
    """Test the calc module."""

    def test_add(self):
        """Test the add function."""
        self.assertEqual(calc.add(2, 4), 6)
        self.assertEqual(calc.add(0, 0), 0)
        self.assertEqual(calc.add(-4, 4), 0)

    def test_subtract(self):
        """Test the subtract function."""
        self.assertEqual(calc.subtract(2, 4), -2)
        self.assertEqual(calc.subtract(0, 0), 0)
        self.assertEqual(calc.subtract(-1, 1), -2)

    def test_multiply(self):
        """Test the multiply function."""
        self.assertEqual(calc.multiply(2, 4), 8)
        self.assertEqual(calc.multiply(0, 0), 0)
        self.assertEqual(calc.multiply(-1, 1), -1)

    def test_divide(self):
        """Test the divide function."""
        self.assertEqual(calc.divide(4, 2), 2)
        self.assertEqual(calc.divide(-4, -2), 2)
        self.assertEqual(calc.divide(4, -2), -2)
        with self.assertRaises(ZeroDivisionError):
            calc.divide(4, 0)

    def test_power(self):
        """Test the power function."""
        self.assertEqual(calc.power(2, 4), 16)
        self.assertEqual(calc.power(0, 0), 1)
        self.assertEqual(calc.power(-1, 0), 1)

    def test_sqrt(self):
        """Test the sqrt function."""
        self.assertEqual(calc.sqrt(4), 2)
        self.assertRaises(ValueError, calc.sqrt, -1)
