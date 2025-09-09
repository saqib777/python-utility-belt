import unittest
from utils.math_tools import factorial, is_prime

class TestMathTools(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_is_prime_true(self):
        self.assertTrue(is_prime(7))

    def test_is_prime_false(self):
        self.assertFalse(is_prime(8))

    def test_gcd(self):
        from utils.math_tools import gcd
        self.assertEqual(gcd(12, 8), 4)

    def test_lcm(self):
        from utils.math_tools import lcm
        self.assertEqual(lcm(12, 8), 24)


if __name__ == "__main__":
    unittest.main()
