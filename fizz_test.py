import unittest
from fizz_checker import FizzChecker

class FizzTest(unittest.TestCase):

    def test_is_Fizz(self):

        actual = FizzChecker.is_fizz(i % 3 == 0)

        self.