# Warunki arytmetyczne
cost = 6
product = "cebula"

if cost >= 3:
    print("Nie kupuj bo za drogie")
else:
    print("Kupuj bo tanio!")

# Operatory: not, and, or
if product == "cebula" and cost < 3:
    print("Kupuj tę cebulę, Polaku!")
else:
    print("Unikaj jak ognia, bo bardzooo drogiee")

# and - oba warunki muszą być spełnione
# or - jeden z warunków musi być spełniony

# Operator in / not in (później) oraz przedziały
# Przypadek: Liczby są z zakresu 2.0 do 5.0

grade = 4.890

if 2 <= grade <= 5:
    print("Ocena prawidłowa")
else:
    print("Ocena nieprawidłowa")



grade = 2.0

#if grade == "2.0" or "3.0"
    #print("Ocena prawidłowa")
#else:
    #print("Ocena nieprawidłowa")

# elif - sprawdza kolejny warunek, jak poprzedni był nieprawdziwy

cost = 2
product = "cebula"

if product == "cebula" and cost <= 3:
    print("Kupuj tę cebulę")
elif product == "marchewka" and cost <= 4.5:
    print("Kupujesz marchewkę")
elif product == "cola" and cost <= 19.99:
    print("Kupujesz coca-cole")
else:
    print("Wychodzisz bez zakupów")