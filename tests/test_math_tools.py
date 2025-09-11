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

import unittest
from utils.math_tools import factorial_iterative, factorial_recursive

class TestMathTools(unittest.TestCase):
    def test_factorial_iterative(self):
        self.assertEqual(factorial_iterative(5), 120)
        self.assertEqual(factorial_iterative(0), 1)
        with self.assertRaises(ValueError):
            factorial_iterative(-1)

    def test_factorial_recursive(self):
        self.assertEqual(factorial_recursive(5), 120)
        self.assertEqual(factorial_recursive(1), 1)
        with self.assertRaises(ValueError):
            factorial_recursive(-3)



if __name__ == "__main__":
    unittest.main()
