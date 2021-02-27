class FizzBuzzChecker:

    @staticmethod
    def is_fizzbuzz(I):
        if I % 3 == 0 and I % 5 == 0:
            print("Bob : FizzBuzz")
        if I % 3 == 0:
            print("Bob : Fizz")
        if I % 5 == 0:
            print("Bob : Buzz")
        else:
            print("Bob : ",I)