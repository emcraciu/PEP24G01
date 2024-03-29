nr = input("Cate carti doriti sa adaugati in biblioteca?")
lista_carti = []
for i in range(int(nr)):
    nume_carte = input('introduceti numele cartii: ')
    autor_carte = input('introduceti autor carte: ')
    anul_publicarii = int(input('introduceti anul publicarii: '))

    dict_carte = {'nume': nume_carte, 'autor': autor_carte, 'an': anul_publicarii}
    lista_carti.append(dict_carte)

print(lista_carti)

an_introdus = int(input('introduceti an: '))
for dictio in lista_carti:
    for key, value in dictio.items():
        if key == 'an' and int(value) > an_introdus:
            print(f"{list(dictio.values())[0]} a fost publicata dupa {an_introdus}.")

