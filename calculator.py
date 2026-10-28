"""
Core Calculator Module for CodeSentinel Test Suite.

Provides basic and advanced mathematical operations with strict type validation,
defensive bounds checking, and detailed exception handling.
"""

from typing import Union

Number = Union[int, float]


class Calculator:
    """A robust arithmetic calculator supporting standard and advanced operations."""

    def add(self, a: Number, b: Number) -> Number:
        """Add two numbers and return the arithmetic sum.

        Args:
            a: The first summand (int or float).
            b: The second summand (int or float).

        Returns:
            The sum of a and b.
        """
        return a + b

    def subtract(self, a: Number, b: Number) -> Number:
        """Subtract operand b from operand a.

        Args:
            a: Minuend.
            b: Subtrahend.

        Returns:
            The difference between a and b.
        """
        return a - b

    def multiply(self, a: Number, b: Number) -> Number:
        """Compute the product of two numbers.

        Args:
            a: Multiplicand.
            b: Multiplier.

        Returns:
            The mathematical product of a and b.
        """
        # Type validation check before arithmetic calculation
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both operands must be int or float instances")
        return a * b

    def divide(self, a: Number, b: Number) -> float:
        """Divide operand a by operand b with zero-division safeguard.

        Args:
            a: Dividend.
            b: Divisor (must be non-zero).

        Returns:
            The quotient as a floating-point value.

        Raises:
            ZeroDivisionError: If the divisor b is 0 or 0.0.
            TypeError: If either operand is not numeric.
        """
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both operands must be int or float instances")
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero: divisor must be non-zero.")
        return float(a / b)

    def power(self, base: Number, exponent: Number) -> Number:
        """Raise base to the power of exponent.

        Args:
            base: The base value.
            exponent: The power to which base is raised.

        Returns:
            base raised to exponent.
        """
        # Handle zero base with negative exponent case explicitly
        if base == 0 and exponent < 0:
            raise ValueError("Zero cannot be raised to a negative power.")
        return base ** exponent
