#łańcuch znakowy jako kolekcja danych

txt = "Ala ma kota."

# Warunek na podstawie zbioru
if "pies" in txt:
    print("Tak, Ala ma kota")

# Metody dla str
print(len(txt))
print(txt.upper())
print(txt)

# Indeksowanie
# W kolekacji znaków poszczególne elementy (czyli litery i inne znaki) posiadają indeksy.
# Indeksy mają numery: 0...(len-1)

print(txt[0])       # Wyświetl 1 znak (znak o indeksie 0).
print(txt[:4])      # <0, 4) | <0, 3> Wyświetla znaki od ineksach 0-3
print(txt[2:8])     # ,2, 8) | <2, 7>
print(txt[3:])     # <3, len) | <3, len-1>
print(txt[2:8:2])   # <2,7> co drugi = <2, 4, 6>
print(txt[::3])     # <caly tekst> co trzeci
print(txt[::-1])    # zapisa od końca (lustrzane odbicie)

# Python przypisuje indeksy o wartościach dodatnich i ujemnych. Przypisuje je od poczatku tekstu, zaczynając od 0,
# ale również przypisuje je od końca tekstu, zaczynając od -1.

#  H  E  L  L  O
#  0  1  2  3  4
# -5 -4 -3 -2 -1

