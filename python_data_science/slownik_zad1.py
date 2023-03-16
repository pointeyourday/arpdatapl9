

def add_contacts(con_dict: dict, key: str, value: str) -> None:
    if key in con_dict.keys():
        print("Kontakt istnieje")
    else:
        con_dict[key] = value
        print("Kontakt dodano")


contacts2 = {
    "Ewa": "00012001"
}

add_contacts(

)