# zad 1

# n = int(input("Podaj liczbę: "))
#
# number = 0
#
# while number <= n:
#     if number % 2 == 0:
#         print(number)
#     number = number + 1

# lub

# n = int(input("Podaj liczbę: "))
# i = 0
# while i <= n:
#     print(i)
#     i += 2


# zad 2.
#
# n = 10
# while n >= 2:
#     print("Pierwiastek liczby," n, "to:", n ** 0.5)
#     n -= 1

#zad. 3
# Napisz program, ktory sumuje wszystkie liczby całkowite z danego zakresu. Początek i koniec zakresu
# podaje użytkownik.
# Np. start = 10, end = 12, wynik - 33

start = int(input("Podaj start: "))
end = int(input("Podaj koniec: "))
result = 0

for i in range(start, end + 1):
    result += i

print("Wynik", result)
print("Wynik", sum(range(start, end +1)))