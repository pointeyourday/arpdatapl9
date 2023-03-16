# Napisz funkcję manage_list, która przyjmuje dwa argumenty:
#     - Opcja: dodaj, usuń
#     - Wartość
# Jeżeli wybraliśmy dodaj, wykonany jest append
# Jeżeli usuń - wykonujemy pop()
# Funkcja niczego nie zwraca.

animals = ["Kot", "Pies", "Słoń", "Żółw", "Chomik", "Papuga"]
print(animals)

def manage_list (option, value):
    if option == "dodaj":
        animals.append(value)
    elif option == "usuń":
        animals.pop()

manage_list("dodaj", "Kanarek")
print(animals)

manage_list("usuń", "Kot")
print(animals)



