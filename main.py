def fizzbuzz(number):
    if number % 15 == 0 :
        return "FizzBuzz"
    elif number % 3 == 0 :
        return "Fizz"
    elif number % 5 == 0 :
        return "Buzz"
    elif number <= 0 :
        return "Error"
    else :
        return number