while True:
    try:
        nr = int(input("Cate carti doriti sa adaugati in biblioteca? "))
        break
    except:
        print("Invalid output, please try again!")
        continue

lista_carti = []

for i in range(nr):
    print(f"{10 * '='} Cartea {i + 1} {10 * '='}")
    nume_carte = input("Care este numele cartii? ")
    nume_autor = input("Care este numele autorului? ")
    an_publicare = input("Care este anul publicarii? ")
    dict_carte = {'nume': nume_carte, 'autor': nume_autor, 'an': an_publicare}
    lista_carti.append(dict_carte)

print("Cartile dumneavoastra sunt: ")
for dict in lista_carti:
    print(dict)

start_an_publicatie = int(input("Care este anul publicatiei de start? "))
for dict in lista_carti:
    for key, value in dict.items():
        if key == 'an' and int(value) > start_an_publicatie:
            print(f"{list(dict.values())[0]} a fost publicata dupa {start_an_publicatie}.")
