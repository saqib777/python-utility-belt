"""
String Tools
------------
This module contains simple utility functions to make working with strings easier.
Each function is kept simple and well-documented for learners.
"""

def reverse_string(s: str) -> str:
    """
    Reverse a given string.
    """
    return s[::-1]


def is_palindrome(s: str) -> bool:
    """
    Check if a given string is a palindrome.
    """
    s = s.lower().replace(" ", "")
    return s == s[::-1]
