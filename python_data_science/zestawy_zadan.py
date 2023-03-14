#zad 1

total_answers = int(input("Podaj liczbę wszystkich pytań: "))
correct_answers = int(input("Podaj liczbę prawidłowych odpowiedzi: "))

percent = int((correct_answers / total_answers) * 100)

if 100 <= percent <= 90:
    print("Ocena: 5.0")
elif 89 <= percent <= 74:
    print("Ocena: 4.5")
elif percent >= 0.70 and procent <= 0.75:
    print("Ocena: 4.0")
elif procent >= 0.60 and procent <= 0.69:
    print("Ocena: 3.5")
elif procent >= 0.50 and procent <= 0.59:
    print("Ocena: 3.0")
else:
    print("Ocena: 2.0")


#zad 2

def show_temp_status (temperature):
    if temperature > 37.1:
        return "Gorączka"
    elif 36.9 <= temperature <= 37.1:
        return "Stan podgorączkowy"
    elif 36.4 <= temperature <= 36.8:
        return "Norma"
    else:
        return "Wychłodzenie"

print(show_temp_status(38))
print(show_temp_status(36.6))
print(show_temp_status(36.75))
print(show_temp_status(36.2))



