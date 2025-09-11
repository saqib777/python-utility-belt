import unittest
from utils.string_tools import reverse_string, is_palindrome

class TestStringTools(unittest.TestCase):

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")

    def test_is_palindrome_true(self):
        self.assertTrue(is_palindrome("madam"))

    def test_is_palindrome_false(self):
        self.assertFalse(is_palindrome("hello"))

    def test_count_vowels(self):
        from utils.string_tools import count_vowels
        self.assertEqual(count_vowels("hello"), 2)
        self.assertEqual(count_vowels("sky"), 0)

import unittest
from utils.string_tools import is_anagram

class TestStringTools(unittest.TestCase):
    def test_is_anagram(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("triangle", "integral"))
        self.assertFalse(is_anagram("hello", "world"))


if __name__ == "__main__":
    unittest.main()
