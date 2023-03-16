# Lista składana
numbers = []
for i in range(11):
    numbers.append(2 ** i)
print(numbers)

numbers_v2 = [2 ** i for i in range(11)]
print(numbers_v2)

# Ciekawostka: słownik składany
power_for_2 = {i:2**i for i in range(11)}
print(power_for_2)