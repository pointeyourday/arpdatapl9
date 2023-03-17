# Zadanie 01
# Napisać funkcję, która zamienić stopnie Celsjusza na Kelwina.
# Funkcja przyjmuje jako argument temperaturę w C, a funkcja zwraca temperaturę w K.
# Więcej informacji o konwersji: https://www.rapidtables.org/pl/convert/temperature/how-celsius-to-kelvin.html
# Obie wartości maja być typu float


# def temp_convert(deg_c):
#     deg_c = float(deg_c)
#     deg_k = deg_c + 273.15
#     return deg_k
#
#
# print(temp_convert(14))
# print(temp_convert(0))
# print(temp_convert(-273.15))


# Alternatywne rozwiązanie "pro". Z typowaniem danych.

def temp_convert(deg_c: float) -> float:
    deg_k = deg_c + 273.15
    return deg_k


print(temp_convert(14))
print(temp_convert(-273.15))
print(temp_convert(0))





