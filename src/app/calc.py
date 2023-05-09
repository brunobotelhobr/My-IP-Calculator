"""
Do math calculations.

This script can be imported as a module and allows the user
to make mathematical calc.

Examples:
    >>> from app import calc.Calculator sd as calc
    >>> calc.add(2, 4)
    6.0
    >>> calc.multiply(2.0, 4.0)
    8.0
    >>> from app import calc
    >>> calc.divide(4.0, 2)
    2.0

The module contains the following functions:

- `add` - returns the sum of two numbers
- `subtract` - returns the difference of two numbers
- `multiply` - returns the product of two numbers
- `divide` - returns the quotient of two numbers
- `power` - returns the base to the power of the exponent
- `sqrt` - returns the square root of a number
"""

from typing import Union


class Calculator:
    """Calculator class."""

    def add(self, a: Union[float, int], b: Union[float, int]) -> float:
        """
        Do addition of two numbers.

        Examples:
            >>> add(4.0, 2.0)
            6.0
            >>> add(4, 2)
            6.0

        Args:
            a: first number
            b: second number

        Returns:
            sum of the first and the second number
        """
        return float(a + b)

    def subtract(
        self, a: Union[float, int], b: Union[float, int]
    ) -> float:  # pylint: disable=invalid-name
        """
        Do subtraction of two numbers.

        Examples:
            >>> subtract(4.0, 2.0)
            2.0
            >>> subtract(4, 2)
            2.0

        Args:
            a: minuend
            b: subtrahend

        Returns:
            the difference between the minuend minus the subtrahend
        """
        return float(a - b)

    def multiply(
        self, a: Union[float, int], b: Union[float, int]
    ) -> float:  # pylint: disable=invalid-name
        """
        Do multiplication of two numbers.

        Examples:
            >>> multiply(4.0, 2.0)
            8.0
            >>> multiply(4, 2)
            8.0

        Args:
            a: first number
            b: second number

        Returns:
            the product of the two numbers
        """
        return float(a * b)

    def divide(
        self, a: Union[float, int], b: Union[float, int]
    ) -> float:  # pylint: disable=invalid-name
        """
        Do division of two numbers.

        Examples:
            >>> divide(4.0, 2.0)
            2.0
            >>> divide(4, 2)
            2.0
            >>> divide(4, 0)
            Traceback (most recent call last):
            ...
            ZeroDivisionError: division by zero

        Args:
            a: dividend
            b: divisor

        Raises:
            ZeroDivisionError: gets raised when the divisor is `0`

        Returns:
            the quotient
        """
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return float(a / b)

    def power(
        self, base: Union[float, int], exponent: Union[float, int] = 2.0
    ) -> float:  # pylint: disable=invalid-name
        """
        Do exponentiation of a number.

        Examples:
            >>> power(4.0, 2.0)
            16.0
            >>> power(4, 2)
            16.0
            >>> power(4)
            16.0

        Args:
            base: the base number
            exponent: the exponent used

        Returns:
            the result of taking the base to the exponent
        """
        return float(base**exponent)

    def sqrt(
        self, a: Union[float, int]
    ) -> float:  # pylint: disable=invalid-name
        """
        Do square root of a number.

        Examples:
            >>> sqrt(4.0)
            2.0
            >>> sqrt(4)
            2.0

        Args:
            a: the number that you want to take the square root of

        Raises:
            ValueError: raises if `a` is below `0`

        Returns:
            the square root of `a`
        """
        if a < 0:
            raise ValueError("math domain error")
        return float(a ** (1 / 2))
