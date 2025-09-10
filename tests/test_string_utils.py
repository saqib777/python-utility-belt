import unittest
from utils.string_utils import is_palindrome, reverse_string

class TestStringUtils(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("hello"))

    def test_reverse_string(self):
        self.assertEqual(reverse_string("hello"), "olleh")
        self.assertEqual(reverse_string("Python"), "nohtyP")

if __name__ == '__main__':
    unittest.main()
