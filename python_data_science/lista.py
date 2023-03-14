# Lista

animals = ["Kot", "Pies", "Słoń", "Żółw", "Chomik", "Papuga"]
numbers = [2, 5, 10, 3]

values = [3, 4.67, "LOL", True, 11, "xD"]
# Listy w Pythonie pozwalają do jednej listy przyporządkować różne typy danych. Jednak jest to
# zła praktyka, nie należy tak robić.

# Pusta lista: empty = [] lub empty = list()

# Lista posiada również funkcjonalności:
# print(len(animals))  # len
# print(animals[0], animals[-1], animals[2:4])  # indeksy
#
# print(sum(numbers), max(numbers), min(numbers))

# DODAWANIE WARTOŚCI
#   .append dodaje jeden element do listy
print(animals.append("Szynszyla"))
print(animals)

# extend doaje kilka elementów w formie listy
animals.extend(["Mysz", "Kanarek"])
print(animals)

# insert dodaje pojedynczy element pod podanym ineksem. Jeśli pod tym indeksem istnieje już element, to lista zostanie
# przesunięta w prawo. Element może być listą, ale zostanie dodana ona jako jeden obiekt.
animals.insert(1, "Krokodyl")
print(animals)
animals.insert(0, ["A, B"])
print(animals)

# USUWANIE WARTOŚCI
# Jeśli na liście jest dany element, zostanie on usunięty.
# Jeśli na liście jest kilka takich samych elementów to zostanie usunięty ten najbliżej początku listy
# (program skanuje listę od indeksu 0 i usuwa pierwszy napotkany zadany element).
animals.remove("Szynszyla")
print(animals)

animals.pop()  # Jeżeli nie podamy idx, usuwamy ostatni element
print(animals)
animals.pop(2)
print(animals)

deleted_value = animals.pop(5)
print(animals, deleted_value)


deleted_args = []

deleted_args.append(animals.pop())
print(animals)
deleted_args.append(animals.pop(2))
print(animals)

deleted_value = animals.pop(0)
deleted_args.append(deleted_value)
print(animals, deleted_args)


# MODYFIKACJA WARTOŚCI
animals[0] = "Mrówka"
print(animals)