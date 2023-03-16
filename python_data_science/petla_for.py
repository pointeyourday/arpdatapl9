# Pętle for
# działa dla sekwencji danych
# 1. Łańcuch znakowy

# for x in "KOTEK":
#     print("Litera:", x)


# 2. Łańcuch znakowy -> lista
for word in "Ala ma kota".split(" "):
    print("Słowo:", word)

# 3. Lista/Krotka
accounts = [
    ("A001", "100600", 250.50),
    ("B001", "200800", 199.97),
    ("A002", "600100", 213.90)
]

for element in accounts:
    print("Klient:", element)


# 4. Sekwencja liczb (range)
# range(start, end, step)

# 4a. Ciąg malejący
for i in range(10, -1, -1):
    print(i)