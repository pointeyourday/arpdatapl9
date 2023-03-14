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
