# Słownik - zestaw wartości w pewnym mapowaniu ???
# W słowniku do każdego klucza (np. Imię i nazwisko przypisana jest jakaś wartość (np. numer telefonu).

contacts = {
    "Adam": "111111111",
    "Ewelina": "222222222",
    "Piotr": "333333333"
}

print(len(contacts))

# Dostęp do kluczy, wartości, elementów
print(contacts.keys())
print(contacts.values())
print(contacts.items())

if "Adam" in contacts.keys():
    print ("Kontakt istnieje.")

# Dodawanie nowych kluczy
contacts["Iza"] = "444444444"
print(contacts)
contacts["Adam"] = "000000000" # <<<-- UWAGA! Program nadpisze wartość na kluczu!
print(contacts)

# Wyświetlanie wybranej wartości
print(contacts["Ewelina"])
# print(contacts[Bozydar])  # <<--- Jeli wpiszemy klucz, ktry nie istnieje wyskoczy błąd (error)

print(contacts.get("Ewelina", "Kontakt nie istnieje"))  #<<--- Pierwszy argument określa wartość poszukiwaną,
# drugi zawiera komunikat, który należy wyświetlić, jeśli dany klucz nie istnieje.

# 1
print(contacts.get("Bozydar", "Kontakt nie istnieje"))

# 2
if "Bozydar" in contacts.keys():
    print(contacts["Bozydar"])
else:
    print(-1)

# Usuwannie kluczy (oraz ich wartości)
contacts.pop("Adam")  # W tym przypadku pop nie może być bez argumentu.
del contacts["Iza"]  # Dla ciekawskich

# Przepisywanie pod nowy klucz
contacts["Mateusz"] = contacts.pop("Ewelina")

print(contacts)


