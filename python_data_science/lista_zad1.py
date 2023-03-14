# Napisz funkcję manage_list, która przyjmuje dwa argumenty:
#     - Opcja: dodaj, usuń
#     - Wartość
# Jeżeli wybraliśmy dodaj, wykonany jest append
# Jeżeli usuń - wykonujemy pop()
# Funkcja niczego nie zwraca.

animals = ["Kot", "Pies", "Słoń", "Żółw", "Chomik", "Papuga"]
print(animals)

def manage_list (działanie, wartość):
    if działanie == "dodaj":
        animals.append(wartość)
    elif działanie == "usuń":
        animals.pop(wartość)
    else:
        print("błąd polecenia")

manage_list("dodaj", "Tygrys")
print(animals)

manage_list("ddaj", 2)
print(animals)



