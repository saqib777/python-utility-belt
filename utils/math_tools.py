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

def gcd(a: int, b: int) -> int:
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers
    using the Euclidean algorithm.
    Example: gcd(12, 8) -> 4
    """
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """
    Calculate the Least Common Multiple (LCM) of two numbers.
    Uses gcd(a, b) for calculation.
    Example: lcm(12, 8) -> 24
    """
    return abs(a * b) // gcd(a, b)
