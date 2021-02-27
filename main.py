I = int(input("Alice, entrez un chiffre : "))
if I < 1:
    print("Bob : Chiffre invalide")
elif I % 3 == 0 and I % 5 == 0:
    print("Bob : FizzBuzz")
elif I % 3 == 0:
    print("Bob : Fizz")
elif I % 5 == 0:
     print("Bob : Buzz")
else:
    print("Bob : ",I)