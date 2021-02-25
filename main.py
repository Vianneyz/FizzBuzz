I = -4
while I < 101:
    if I < 1:
        print("Erreur : chiffre invalide")
    elif I % 3 == 0 and I % 5 == 0:
        print("FizzBuzz")
    elif I % 3 == 0:
        print("Fizz")
    elif I % 5 == 0:
        print("Buzz")
    else:
        print(I)
    I += 1