import unittest
from main import fizzbuzz

class FizzBuzzTest(unittest.TestCase):

    def test_call_FizzBuzz_Returns_1_When_Passed_1(self):
        self.assertEqual(fizzbuzz(1), 1)

    def test_call_FizzBuzz_Returns_2_When_Passed_2(self):
        self.assertEqual(fizzbuzz(2), 2)

    def test_call_FizzBuzz_Returns_Fizz_When_Passed_3(self):
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_call_FizzBuzz_Returns_Buzz_When_Passed_5(self):
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_call_FizzBuzz_Returns_Fizz_When_Passed_Multiple_Of_3(self):
        self.assertEqual(fizzbuzz(6), "Fizz")

    def test_call_FizzBuzz_Returns_Buzz_When_Passed_Multiple_Of_5(self):
        self.assertEqual(fizzbuzz(10), "Buzz")

    def test_call_FizzBuzz_Returns_FizzBuzz_When_Passed_15(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_call_FizzBuzz_Returns_Error_When_Passed_0(self):
        self.assertTrue(fizzbuzz(0), "Error")

    def test_call_FizzBuzz_Returns_Error_When_Passed_neg(self):
        self.assertLess(fizzbuzz(0), "Error")

if __name__ == "__main__":
    unittest.main()