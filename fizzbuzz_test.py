import unittest
from unittest.case import TestCase
from main import fizz_buzz

class FizzBuzzTest(unittest.TestCase):
    # def test_canCallFizzBuzz(self):
    # fizzbuzz.fizz_buzz(1)

    def checkValWithExpected(val,expected):
        ret = fizzbuzz.fizz_buzz(val)
        self.assertEqual(ret,expected)

    def test_callFizzBuzzReturns1WhenPassed1(self):
        # self.assertEqual(fizzbuzz.fizz_buzz(1), "1")
        self.chexkValWithExpected(1, "1")

    def test_callFizzBuzzReturns2WhenPassed2(self):
        # self.assertEqual(fizzbuzz.fizz_buzz(2), "2")
        self.chexkValWithExpected(2, "2")

    def test_callFizzBuzzReturnsFizzWhenPassed3(self):
        self.checkValWithExpected(3, "Fizz")

    def test_callFizzBuzzReturnsBuzzWhenPassed5(self):
        self.checkValWithExpected(5, "Buzz")

    def test_callFizzBuzzReturnsFizzWhenPassedMultipleOf3(self):
        self.checkValWithExpected(6, "Fizz")

    def test_callFizzBuzzReturnsBuzzWhenPassedMultipleOf5(self):
        self.checkValWithExpected(10, "Buzz")

    def test_callFizzBuzzReturnsFizzBuzzWhenPassed15(self):
        self.checkValWithExpected(15, "FizzBuzz")