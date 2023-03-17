# Zadanie 02
# Napisać funkcję, która jako argument przyjmuje dowolny łańcuch znakowy,
# a następnie zwraca słownik zliczający ilość wystąpień każdego słowa (kot =/= kota).
# Podpowiedź możemy użyć metody split(" ").

txt = "lubię lody lody są super są zimne i są smaczne " \
      "jak będę senior python developer i będę mieć pieniądze to kupię fabrykę lodów " \
      "będę jeść lody każdego dnia"


# def counter(text: str) -> dict:
#     word = text.split()
#     result = {}
#     for c in word:
#         if c is not result.keys():
#             result[c] = word.count(c)
#     return result
#
#
# print(counter(txt))


def counter_2(text: str) -> dict:
    word = text.split()
    result = {}
    for c in word:
        if c not in result.keys():
            result[c] = 1
        else:
            result[c] += 1
    return result


print(counter_2(txt))