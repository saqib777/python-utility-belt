def is_palindrome(text: str) -> bool:
    """Check if a string is a palindrome."""
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    return cleaned == cleaned[::-1]


def reverse_string(text: str) -> str:
    """Reverse a given string."""
    return text[::-1]
