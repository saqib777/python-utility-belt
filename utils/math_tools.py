"""
Math Tools
----------
This module provides basic math utility functions.
"""

def factorial(n: int) -> int:
    """
    Calculate the factorial of a number.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return 1 if n == 0 else n * factorial(n - 1)


def is_prime(n: int) -> bool:
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
