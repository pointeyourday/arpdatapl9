# Napisz funkcję, która przyjmuje łańcuch znakowy (same małe litery).
# Funkcja ma zawrócić słownik (return), który zawiera informacje w postaci:
#   klucz -litera
#   wartość - ilość wystapień litery w tekscie
# tekst: alamakotaakotmapierdolca

txt = "alamakotaakotmapierdolca"

def char_counter(text: str) -> dict:
    result = {}
    for c in text:
        if c not in result.keys():
            result[c] = text.count(c)

    return result

print(char_counter(txt))

def char_counter_2(text: str) -> dict:
    result = {}
    for c in text:
        if c in result.keys():
            result[c] += 1
        else:
            result[c] = 1

    return result

print(char_counter_2(txt))




