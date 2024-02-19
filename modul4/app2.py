def medie(numbers_list):
    return sum(numbers_list) / len(numbers_list)


def suma(numbers_list):
    return sum(numbers_list)


def putere(numbers_list):
    result = []
    for number in numbers_list:
        result.append(number ** 2)
    return result


meniu = {
    "1": medie,
    "2": suma,
    "3": putere
}
num_list = []
while True:
    number = input("Type a number: ")
    if number.lower() == "x":
        break
    try:
        number = float(number)
    except Exception:
        print("Invalid number. Type again")
        continue
    num_list.append(number)

methods_dict = {1: 'Media numerelor', 2: 'Suma numerelor', 3: 'Putere numerelor', 4: 'Iesire'}
for option_number, option_name in methods_dict.items():
    print(f"{option_number}. {option_name}")
choice = input("Introduceti optiunea dvs: ")
result = meniu.get(choice)(num_list)
print(f"Rezultatul: {result}")
