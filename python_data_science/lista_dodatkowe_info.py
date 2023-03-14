# Napisz funkcję manage_list, która przyjmuje dwa argumenty:
#     - Opcja: dodaj, usuń
#     - Wartość
# Jeżeli wybraliśmy dodaj, wykonany jest append
# Jeżeli usuń - wykonujemy pop()


animals = ["Kot", "Pies", "Słoń", "Żółw", "Chomik", "Papuga"]
print(animals)

def manage_list_poprawna(działanie, wartość, input):
    result = input.copy()
    if działanie == "dodaj":
        result.append(wartość)
        return result
    elif działanie == "usuń":
        result.pop(wartość)
        return result
    else:
        print(f"Nieznana komenda: {działanie}")

manage_list_poprawna("dodaj", "Tygrys", animals)
print(animals)

manage_list_poprawna("ddaj", 2, animals)
print(animals)


# xs = [1, 2, 3]
# print("'Poprawna' wersja")
# print(f"Przed wywołaniem funkcji, xs={xs}")
# new_xs = manage_list_poprawna('dodaj', 4, xs)
# print(f"Wynik wywołania funkcji, new_xs={new_xs}")
#
# print(f"Po wywołaniu funkcji, xs={xs}")
#



def adder(x):
    return x + 2

def adder_list(x):
    x.append(2)

# manage_list("dodaj", "mordka")
# print(animals)
#
# manage_list("usuń", 2)
# print(animals)


print("Adder na int")
x = 6
print(x)
x = adder(x)
print(x)


print("Adder na xs")
xs = [1]
print(xs)
adder_list(xs)
print(xs)
