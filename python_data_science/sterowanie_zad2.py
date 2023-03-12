
x = int(input("Podaj liczbę całkowitą: "))


if x % 3 == 0 and x % 5 == 0:
    print("Pif Paf")
elif x % 3 == 0:
    print("Pif")
elif x % 5 == 0:
    print("Paf")
else:
    print("Twoja liczba to: ", x)
